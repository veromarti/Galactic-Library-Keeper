import csv
import json
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
    guardar_visitantes(visitors_list)
    saveJson(visitors_list)
    return visitors_list


def guardar_visitantes(visitors):
    with open('visitors.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=['id','name','species','status'])
        writer.writeheader()
        writer.writerows(visitors)



def saveJson(visitors):
    with open('visitors.json', 'w', newline='',encoding='utf-8') as file:
        json.dump(visitors, file, indent=4, ensure_ascii=False)



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