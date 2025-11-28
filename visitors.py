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
    print(ids)
    existing_id = True
    print("- - - Regitering Visitor - - -\n")
    print("\nEnter Visitor Information\n")

    id = utils.int_entry("ID: ")
    existing_id = find_id(id,ids)
    if existing_id:return visitors_list
        
    elif not existing_id:
        ids.add(id)
        name = utils.str_entry("Name: ")
        species = utils.str_entry("Species: ")
        status = utils.str_entry("Status: ")
        visitor ={'id': id, 
                'name': name, 
                'species': species,
                'status': status}
        visitors_list.append(visitor)
        save_visitors(visitors_list)
        saveJson(visitors_list)
        return visitors_list
    

def save_visitors(visitors):
    with open('visitors.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=['id','name','species','status'])
        writer.writeheader()
        writer.writerows(visitors)


def saveJson(visitors):
    with open('visitors.json', 'w', newline='',encoding='utf-8') as file:
        json.dump(visitors, file, indent=4, ensure_ascii=False)

def show_visitors(*args):

    visitors = load_visitors()

    if not visitors:
        print("\nNo visitors recorded\n")
        return

    print("\n--- VISITORS LIST ---\n")

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

        matches = True
        for f in args:
            f = str(f).lower()
            if not any(f in str(field).lower() for field in visitor_tuple):
                matches = False
                break

        if matches:
            print(visitor_tuple)
            

def find_visitor(ID, visitors):
    """This function receives the name of a book and the list of dictionaries were the books 
        information is stored, then it iterates the list, and returns the dictionary of the book
        and the position inside the list, if the book is not found it returns None for both elements
    """

    for item in visitors:
        if str(ID) in item['id']:
            element = visitors.index(item)
            return item, element
    return None, None

def update_visitor(ID, visitors):
    """This function receives the name of the book to be updated,the list of dictionaries, the new 
        price and new quantity it uses the find_book() function to obtain the book information, 
        then it overwrites the price and quantity values. at the end the .csv file is updated 
        accordingly and returns the updated list of dictionaries
    """

    item, element = find_visitor(ID, visitors)
    if item is not None:
        if item['status'].lower() == 'active':
            print(input("\nChange status from Active to Retired (y/n): "))
            item['status'] = 'retired'
        elif item['status'].lower() == 'retired':
            print(input("\nChange status from Retired to Active (y/n): "))
            item['status'] = 'active'

        save_visitors(visitors)
        saveJson(visitors)
        print("\nStatus updated succesfully")

    else:print("\nNo visitor found\n")
    return visitors

def listar_visitantes(*args):
    """
    Lista visitantes desde el archivo CSV.
    
    Si *args está vacío → muestra todos los visitantes.
    Si *args tiene valores → filtra por coincidencias exactas.
    
    Cada visitante se imprime como una TUPLA.
    """

    # if not os.path.exists(ARCHIVO):
    #     print("⚠ No hay visitantes registrados.")
    #     return

    print("\n--- LISTA DE VISITANTES ---\n")

    with open("visitors.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)

        encabezado = next(reader, None)
        print(encabezado)

        for fila in reader:
            visitante = tuple(fila)

            # Si no se pasaron filtros → mostrar todos
            if not args:
                print(visitante)
                continue

            # Si hay filtros, se compara cada argumento con cada campo del visitante
            coincide = True
            for filtro in args:
                filtro = str(filtro).lower()

                # Si el filtro no aparece en ningún campo → descartar
                if not any(filtro in campo.lower() for campo in visitante):
                    coincide = False
                    break

            # Mostrar solo los que cumplen todos los filtros
            if coincide:
                print(visitante)