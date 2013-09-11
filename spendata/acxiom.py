import csv 
import codecs
from spendata.models import AcxiomData, ACXIOM_FIELD_MAPPING

def read_into_db():
    """ Reading the (old) Acxiom CSV file into the database """
    rowmap = {}
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
                    acxiom = AcxiomData()
                    for r in rowmap.keys():
                        if not row[rowmap[r]]:
                            continue
                        setattr(acxiom, ACXIOM_FIELD_MAPPING[r], row[rowmap[r]])
                    acxiom.save()
                except Exception as e:
                    print repr(row)


# Record ID - 10 character alpha/numeric code for a specific record for a business (may change month to month)
# Master Record ID - associated with all the records for one particular business and location
# Thus, the Master Record ID is a consistent and persistent identifier from month to month and from file to file.