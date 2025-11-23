import csv

def load_visitors():
    visitors_list = []
    with open("visitors.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            visitors_list.append(row)
        return visitors_list