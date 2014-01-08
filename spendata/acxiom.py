import csv 
import os
import logging
import codecs
import spendata.models

logger = logging.getLogger(__name__)

#TODO: use bulk inserts wherever possible

def read_into_db():
    """ Reading the (old) Acxiom CSV file into the database """
    rowmap = {}
    logger.info("Reading the (old) Acxiom CSV file into the database")
    with open('fixtures/acxiom_seattle.csv','rU') as csvfile:
        reader = csv.reader(csvfile)
        firstline = True
        for row in reader:
            if firstline:
                firstline = False
                for (colnum, title) in enumerate(row):
                    rowmap[title] = colnum
                continue
            if row[rowmap['BusinessName']]:
                try:
                    acxiom = spendata.models.AcxiomData()
                    for r in rowmap.keys():
                        if not row[rowmap[r]]:
                            continue
                        setattr(acxiom, spendata.models.ACXIOM_FIELD_MAPPING[r], row[rowmap[r]])
                    acxiom.save()
                except Exception as e:
                    logger.warn("malformed row: {}".format(repr(row)))


class AcxiomTXTDialect(csv.Dialect):
    delimiter = '\t'
    quotechar = '"'
    doublequote = False
    skipinitialspace = False
    lineterminator = '\n'
    quoting = 0

ACXIOM_FILES = [
    'bdf_groups_ord115967.txt',
    'bdf_index_ord115967.txt',
    'bdf_orgs_ord115967.txt',
    'bdf_primary_ord115967.txt',
    'bdf_primary_Hyderabad_dummydata.txt',
    'ebdf_ord115967.txt',
]

class AcxiomDataReader(object):
    def read_into_db(self):
        for acxiom_file in ACXIOM_FILES:
            self.read_file_into_db(acxiom_file)

    def read_file_into_db(self, acxiom_file):
        #using dictionary to avoid DB calls for duplicates
        logger.info("Reading Acxiom file {} ".format(acxiom_file))
        businessnames = dict()
        with open(os.path.join("fixtures", acxiom_file),'r') as f:
            reader = csv.DictReader(f, dialect=AcxiomTXTDialect)
            model = getattr(spendata.models, self.get_model_name(acxiom_file))
            logger.info("Reading data into {} model".format(model))       
            for n, line in enumerate(reader):
                line = {self.get_field_name(k): v for k, v in line.iteritems()}
                obj, created = model.objects.get_or_create(recordid=line.pop('recordid'), defaults=line)
                #logger.info(line)
                if acxiom_file.startswith("bdf_primary"):
                    businessname = line["businessname"]
                    logger.info("businessname = {}".format(businessname))
                    if not businessname in businessnames:
                        businessnames[businessname] = '1'
                        logger.info("businessname {} is new, inserting".format(businessname))
                        spendata.models.AcxiomBdfPrimaryBusinessName.objects.get_or_create(businessname=businessname)
            logger.info("Inserted {} records".format(n))
                
    def get_model_code(self):
        for acxiom_file in ACXIOM_FILES:
            self.get_model_code_for_file(acxiom_file)

    def get_model_code_for_file(self, acxiom_file):
        name = self.get_model_name(acxiom_file)
        print '\n\nclass {}(models.Model):'.format(name)
        with open(os.path.join("fixtures", acxiom_file),'r') as f:
            reader = csv.DictReader(f, dialect=AcxiomTXTDialect)
            for field_name in reader.fieldnames:
                print '    {field_name:<25} = models.TextField(blank=True)'.format(
                    field_name = self.get_field_name(field_name),
                )

    def get_serializer_code(self):
        for acxiom_file in ACXIOM_FILES:
            name = self.get_model_name(acxiom_file)
            print """
class {0}Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = {0}""".format(name)
        
    def get_views_code(self):
        for acxiom_file in ACXIOM_FILES:
            name = self.get_model_name(acxiom_file)
            print """
class {0}ViewSet(viewsets.ModelViewSet):
    queryset = {0}.objects.all()
    serializer_class = {0}Serializer""".format(name)

    def get_url_code(self):
        for acxiom_file in ACXIOM_FILES:
            name = self.get_model_name(acxiom_file)
            url_name = name[0:6] + "_" + name[6:]
            print "router.register(r'{}', views.{}ViewSet)".format(url_name.lower(), name)

    def get_model_name(self, file_name):
        if file_name == 'ebdf_ord115967.txt':
            name = "EbdfOrd"
        else:
            name = ''.join([s.capitalize() for s in file_name.split("_")[0:2]])
        return "Acxiom{}".format(name)

    def get_field_name(self, field_name):
        if field_name == 'ZIP':
            field_name = 'ZIPCODE'
        elif field_name == 'MODELS':
            field_name = 'MODELSFIELD'
        return field_name.lower()      

# Record ID - 10 character alpha/numeric code for a specific record for a business (may change month to month)
# Master Record ID - associated with all the records for one particular business and location
# Thus, the Master Record ID is a consistent and persistent identifier from month to month and from file to file.
# BDF - Business Directory File
# EBDF - Enhanced BDF

# Organization Table bdf_orgs_ord115967.txt

# The Organization table contains records that share a business name and address with a record in the BDF, where the phone number differs or where the department information is present.  These records represent government offices, universities, hospitals and the like, where multiple departments exist at the same location and where the information in the caption field can be used to identify the department represented by each record.   This department information will reside on this table and link to the BDF based on Master ID.

# Group Table bdf_groups_ord115967.txt
# The Group table separates the professional listings from the main listing for the company. These records share a strict address match (including suite number) and a business category match with a listing in the BDF where the Business Name and the Phone Number are different.  These groups represent law firms, insurance companies, medical practices, etc., where two or more professionals operate a common business.  The listings in the Group tables will tie back to the main listing in the BDF via a Master Record ID.

# Business Directory File (BDF) - One per File bdf_primary_ord115967.txt
# Acxioms Business Directory File (BDF) is a national business listing file that includes all publicly available listings in the U.S and is updated in its entirety every week. 
# Listings include: 
# Business Name and Address
# Telephone number 
# Business Classification Codes (Standard Yellow Page Heading Codes, SIC, BDC, NAICS) Firmagraphics- Sales Volume, Employee Size, Contact Name, Title, etc...
# Latitude/Longitude coordinates with precision codes
# The BDF is the primary file that all of the other tables tie into.


# Enhanced Business Directory File (EBDF) ebdf_ord155967.txt
