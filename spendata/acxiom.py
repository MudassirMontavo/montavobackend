def read_into_db():
    with open('fixtures/acxiom_seattle.csv','rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print ', '.join(row)