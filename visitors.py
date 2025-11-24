import csv
import validation

def load_visitors():
    visitors_list = []
    with open("visitors.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            visitors_list.append(row)
        return visitors_list
    
def id_list(visitors_list):
    ids = set()

    for item in visitors_list:
        ids.add(int(item['id']))

    return ids

def find_id(id, ids):

    if id in ids:
        print("ID already exits")
        return True
    return False

def add_visitor(visitors_list):
    ids = id_list(visitors_list)
    print(ids)
    existing_id = True
    print("- - - Regitering Visitor - - -\n")
    print("\nEnter Visitor Information\n")

    while existing_id:
        id = validation.int_entry("ID: ")
        existing_id = find_id(id,ids)
        
    if not existing_id:
        ids.add(id)
    
    print(ids)

    name = validation.str_entry("Name: ")
    species = validation.str_entry("Species: ")
    status = validation.str_entry("Status: ")
    visitor ={'id': id, 
              'name': name, 
              'species': species,
              'status': status}
    visitors_list.append(visitor)
    return visitors_list
