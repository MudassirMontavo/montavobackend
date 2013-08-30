
import csv 
from spendata.models import AcxiomData, ACXIOM_FIELD_MAPPING

def read_into_db():
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
                acxiom = AcxiomData()
                for r in rowmap.keys():
                    setattr(acxiom, ACXIOM_FIELD_MAPPING[r]) = row[rowmap[r]]
                acxiom.save()