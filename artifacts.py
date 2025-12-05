import utils
import csv

def load_artifacts():
    artifacts_list = []
    with open("artifacts.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            artifacts_list.append(row)
        return artifacts_list
    
def save_artifacts(artifacts):
    with open('artifacts.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=['id','description','rarity','status'])
        writer.writeheader()
        writer.writerows(artifacts)

def add_artifact(artifacts_list):
    ids = id_list(artifacts_list)
    print(ids)
    existing_id = True
    print("- - - Adding Artifact - - -\n")
    print("\nEnter Artifact Information\n")

    while existing_id:
        id = utils.int_entry("ID: ")
        existing_id = find_id(id,ids)

    name = utils.str_entry("Name: ")
    rarity = utils.str_entry("Rarity: ")
    status = utils.str_entry("Status: ")
    artifact ={'id': id, 
              'description': name, 
              'rarity': rarity,
              'status': status}
    artifacts_list.append(artifact)

    save_artifacts(artifacts_list)

    return artifacts_list

def id_list(artifacts_list):
    id_list = []

    for item in artifacts_list:
        id_list.append(int(item['id']))

    return id_list

def find_id(id, id_list):

    if id in id_list:
        print("ID already exits")
        return True
    return False

def show_artifacts(artifacts_list):

    cont = 1
    print('\n')
    print(f'{" # ":^4} {" ID ":^6} {"   DESCRIPTION  ":^18} {" RARITY LEVEL ":^18} {"  STATUS  ":^22}')
    print(f'{"---":^4} {"-----":^6} {"---------------":^18} {"-----------":^18} {"------------":^22}')
            
    for item in artifacts_list:
        print(f"{cont:^4} | {item['id']:<6} | {item['description'].capitalize():<18} | {item['rarity'].capitalize():<18} | {item['status'].capitalize():<22}")
        cont += 1
    print(f'{"---":^4} {"-----":^6} {"---------------":^18} {"-----------":^18} {"------------":^22}')

    return  

def find_artifact(id, artifacts_list):

    for item in artifacts_list:
        if str(id) in item['id']: #volver id int en vez de str
            element = artifacts_list.index(item)
            return item, element
    return None, None

def remove_artifact(artifact, artifacts):

    item, position = find_artifact(artifact, artifacts)
    if position is not None:
        artifacts.pop(position)
        save_artifacts(artifacts)
        print("\nArtifact removed successfully")
        show_artifacts(artifacts)
    else:print("No artifact found\n")
    return artifacts


def art_clasification(artifacts_list,**kwargs):

    print("\nClassification of artifacts by:", kwargs)
    filter = artifacts_list[:] 

    for key, value in kwargs.items():
        key = key.lower()
        value = value.lower()

        filter_list = []

        for artifact in filter:
            value_in_dict = (artifact.get(key,"")).lower()

            if value_in_dict == value:
                filter_list.append(artifact)
            
        filter = filter_list

    if not filter:
        print("\nNo Artifacts Found")
    else:
        print(f"\n{len(filter)} artifact(s) found:\n")
        for art in filter:
            print(f" - ID: {art['id']}, Description: {art['description'].capitalize()}, Rarity: {art['rarity'].capitalize()}, Status: {art['status'].capitalize()}")

    return filter

def remove_artifact(artifact, artifacts_list):
    """This function receives the name of the book to be updated,the list of dictionaries, it uses 
        the find_book() function to obtain the element position inside the inventory list, 
        then it removes the product using .pop() at the end the .csv file is updated accordingly and 
        returns the updated list of dictionaries
    """

    item, position = find_artifact(artifact, artifacts_list)
    if position is not None:
        artifacts_list.pop(position)
        save_artifacts(artifacts_list)
        print("\nArtifact removed successfully")
        show_artifacts(artifacts_list)
    else:print("No artifact found\n")
    return artifacts_list

def artifacts_rarity(artifacts_list):
    cont_low = 0
    cont_high = 0
    cont_prohibid = 0
    cont_medium = 0
    raritys = []

    for item in artifacts_list:
        if item["rarity"].lower() == 'low':
            cont_low += 1
        elif item["rarity"].lower() == 'high':
            cont_high += 1
        elif item["rarity"].lower() == 'medium':
            cont_medium += 1
        elif item["rarity"].lower() == 'prohibid':
            cont_prohibid += 1
    raritys.append({"Low":cont_low})
    raritys.append({"High":cont_high})
    raritys.append({"Medium":cont_medium})
    raritys.append({"Prohibid":cont_prohibid})

    return(raritys)

def artifacts_status(artifacts_list):
    cont_sto = 0
    cont_study = 0
    cont_destroyed = 0
    status = []

    for item in artifacts_list:
        if item["status"].lower() == 'stored':
            cont_sto += 1
        elif item["status"].lower() == 'in study':
            cont_study += 1
        elif item["status"].lower() == 'destroyed':
            cont_destroyed += 1
    status.append({"Stored":cont_sto})
    status.append({"In Study":cont_study})
    status.append({"Destroyed":cont_destroyed})

    return(status)