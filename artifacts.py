import validation
import csv

def load_artifacts():
    artifacts_list = []
    with open("artifacts.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            artifacts_list.append(row)
        return artifacts_list

def add_artifact(artifacts_list):
    ids = id_list(artifacts_list)
    print(ids)
    existing_id = True
    print("- - - Adding Artifact - - -\n")
    print("\nEnter Artifact Information\n")

    while existing_id:
        id = validation.int_entry("ID: ")
        existing_id = find_id(id,ids)

    name = validation.str_entry("Name: ")
    rarity = validation.str_entry("Rarity: ")
    status = validation.str_entry("Status: ")
    artifact ={'id': id, 
              'description': name, 
              'rarity': rarity,
              'status': status}
    artifacts_list.append(artifact)
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

def art_clasification(artifacts_list,**kwargs):

    print("\nClassification of artifacts by:", kwargs)
    filter = artifacts_list[:] #copia independiente de la lista original para no alterar los datos originales

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





def art_clasification(artifacts_list, *args):

    print("\nClassification of artifacts by:", args)

    # Lista donde se guardarán los artefactos filtrados
    filtrados = []

    # Procesar cada condición enviada en *args
    for condicion in args:

        # Separar clave y valor → ejemplo: "rarity=high"
        if "=" in condicion:
            partes = condicion.split("=")
            clave = partes[0].lower()
            valor = partes[1].lower()
        else:
            print(f"Condición inválida: {condicion}")
            continue

        # Crear una lista temporal para esta condición
        filtrados_temporales = []

        # Recorrer cada artefacto
        for artifact in artifacts_list:

            # Obtener el valor dentro del diccionario
            valor_art = artifact.get(clave, "").lower()

            # Comparar
            if valor_art == valor:
                filtrados_temporales.append(artifact)

        # Reemplazar filtrados con los resultados más recientes
        filtrados = filtrados_temporales

    # Mostrar resultados
    if not filtrados:
        print("\nNo Artifacts Found")
    else:
        print(f"\n{len(filtrados)} artifact(s) found:\n")
        for art in filtrados:
            print(
                " - ID:", art["id"],
                ", Description:", art["description"].capitalize(),
                ", Rarity:", art["rarity"].capitalize(),
                ", Status:", art["status"].capitalize(),
                sep=""
            )

    return filtrados





# def update_product(product, inventory, new_price = None, new_quant = None):


#     item, element = find_product(product, inventory)
#     if item is not None:
#         if new_price is not None:
#             item['price'] = new_price
#         if new_quant is not None:
#             item['quantity'] = new_quant
#         print("\nProduct updated succesfully")
#     else:print("\nNo product found\n")
#     return inventory    

# def remove_product(product, inventory):


#     print("- - - Removing product - - -")
#     show_inventory(inventory)
#     item, position = find_product(product, inventory)
#     if position is not None:
#         inventory.pop(position)
#         print("Product removed successfully")
#         show_inventory(inventory)
#     else:print("No product found\n")
#     return inventory    

# def fusion(inventory,inventory_csv):


#     final_inventory = inventory_csv
#     for item in inventory:
#         found_product, x = find_product(item['name'],inventory_csv)
#         if found_product:
#             found_product['price'] = item['price']
#             found_product['quantity'] = item['quantity']
#         else:
#             final_inventory.append(item)
#     return final_inventory
        
# def exit():
#     pass