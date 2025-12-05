import csv
import json
import utils

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
        print("\nID already exits")
        return True
    return False

def add_visitor(visitors_list):
    ids = id_list(visitors_list)
    existing_id = True
    print("- - - Registering Visitor - - -\n")
    print("\nEnter Visitor Information\n")

    id = utils.int_entry("ID: ")
    existing_id = find_id(id,ids)
    if existing_id:return visitors_list
        
    elif not existing_id:
        ids.add(id)
        name = utils.str_entry("Name: ")
        species = utils.str_entry("Species: ")
        status = utils.str_entry("Status: ")
        visitor ={'id': str(id), 
                'name': name, 
                'species': species,
                'status': status}
        visitors_list.append(visitor)
        save_visitors(visitors_list)
        saveJson(visitors_list)
        print("\nVisitor Registered Successfully")
        return visitors_list
    
def save_visitors(visitors):
    with open('visitors.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=['id','name','species','status'])
        writer.writeheader()
        writer.writerows(visitors)

def saveJson(visitors):
    with open('visitors.json', 'w', newline='',encoding='utf-8') as file:
        json.dump(visitors, file, indent=4, ensure_ascii=False)

def show_visitors(visitors, *args):

    if not visitors:
        print("\nNo visitors recorded\n")
        return

    print("\n-------- VISITORS LIST --------\n")
    print("--ID--|--NAME--|--SPECIES--|--STATUS--")


    for v in visitors:
        visitor_tuple = (
            v["id"],
            v["name"],
            v["species"],
            v["status"]
        )

        if not args:
            print(visitor_tuple)
            continue     

        match = True
        for filter in args:
            filter = str(filter).lower()

            if not any(filter in field.lower() for field in visitor_tuple):
                match = False
                break

        if match:
            print(visitor_tuple)   
            

def find_visitor(ID, visitors):

    for item in visitors:
        if str(ID) in item['id']:
            element = visitors.index(item)
            return item, element
    return None, None

def update_visitor(ID, visitors):

    item, element = find_visitor(ID, visitors)
    if item is not None:
        if item['status'].lower() == 'active':
            change = (input("\nChange status from Active to Retired (y/n): "))
            if change.lower() == "y":
                item['status'] = 'retired'
                print("\nStatus updated succesfully")
            
        elif item['status'].lower() == 'retired':
            change = (input("\nChange status from Retired to Active (y/n): "))
            if change.lower() == "y":
                item['status'] = 'active'
                print("\nStatus updated succesfully")

        save_visitors(visitors)
        saveJson(visitors)

    else:print("\nNo visitor found\n")
    return visitors

def remove_visitor(visitor, visitors):

    item, position = find_visitor(visitor, visitors)
    if position is not None:
        visitors.pop(position)
        save_visitors(visitors)
        print("\nVisitor removed successfully")
        show_visitors(visitors)
        saveJson(visitors)
    else:print("No visitor found\n")
    return visitors

def visitors_species(visitors):
    cont_other = 0
    cont_human = 0
    cont_android = 0
    species = []

    for item in visitors:
        if item["species"].lower() == 'other':
            cont_other += 1
        elif item["species"].lower() == 'human':
            cont_human += 1
        elif item["species"].lower() == 'android':
            cont_android += 1
    species.append({"Human":cont_human})
    species.append({"Android":cont_android})
    species.append({"Other":cont_other})

    return(species)

def filter_status(visitors):
    cont = 0

    if not visitors:
        print("\nNo visitors recorded\n")
        return

    for item in visitors:
        if item['status'].lower() == 'retired':
            cont += 1
    
    dict_status = {'retired':cont,
                   'active':len(visitors)-cont
    }

    return dict_status
        
def listar_visitantes(*args):
    """
    Lista visitantes desde el archivo CSV.
    
    Si *args está vacío → muestra todos los visitantes.
    Si *args tiene valores → filtra por coincidencias exactas.
    
    Cada visitante se imprime como una TUPLA.
    """

    print("\n--- LISTA DE VISITANTES ---\n")

    with open("visitors.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)

        encabezado = next(reader, None)
        print(encabezado)

        for fila in reader:
            visitante = tuple(fila)

            if not args:
                print(visitante)
                continue

            coincide = True
            for filtro in args:
                filtro = str(filtro).lower()

                if not any(filtro in campo.lower() for campo in visitante):
                    coincide = False
                    break

            if coincide:
                print(visitante)