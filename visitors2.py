import csv
import json
import os
import utils

def load_visitors():
    visitors_list = []

    if not os.path.exists("visitors.csv"):
        return visitors_list

    with open("visitors.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertir ID a entero para coherencia
            row["id"] = int(row["id"])
            visitors_list.append(row)

    return visitors_list


def id_list(visitors_list):
    ids = set()

    for item in visitors_list:
        ids.add(int(item["id"]))

    return ids



def find_id(id, ids):
    if id in ids:
        print("ID already exists")
        return True
    return False



def add_visitor(visitors_list):
    
    ids = id_list(visitors_list)

    print("\n--- Registering Intergalactic Visitor ---\n")

    while True:
        new_id = utils.int_entry("ID: ")
        if not find_id(new_id, ids):
            break
        print("Try again.\n")

    # Agregar ID al set de IDs
    ids.add(new_id)

    # Capturar resto de información
    name = utils.str_entry("Name: ")
    species = utils.str_entry("Species: ")
    status = utils.str_entry("Status: ")

    visitor = {
        "id": new_id,
        "name": name,
        "species": species,
        "status": status
    }

    visitors_list.append(visitor)


    guardar_visitantes(visitors_list)
    save_json(visitors_list)

    print("\nVisitor successfully registered!\n")
    return visitors_list


def guardar_visitantes(visitors):
    with open("visitors.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "species", "status"])
        writer.writeheader()
        writer.writerows(visitors)


def save_json(visitors):
    with open("visitors.json", "w", encoding="utf-8") as file:
        json.dump(visitors, file, indent=4, ensure_ascii=False)


def list_visitors(*filters):

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

        # Sin filtros → mostrar todos
        if not filters:
            print(visitor_tuple)
            continue

        # Filtros → coincidencias exactas en cualquier campo
        matches = True
        for f in filters:
            f = str(f).lower()
            if not any(f in str(field).lower() for field in visitor_tuple):
                matches = False
                break

        if matches:
            print(visitor_tuple)
