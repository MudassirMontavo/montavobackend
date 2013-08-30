

def read_into_db():
    with open('fixtures/acxiom_seattle.csv','rU') as csvfile:
        reader = csv.reader(csvfile)
        firstline = True
        for row in reader:
            if firstline:
                firstline = False
                continue
            print ', '.join(row)