import csv
import json

def load_visitors():
    visitors = []
    try:
        with open("visitors.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                visitors.append(row)
    except FileNotFoundError:
        pass
    return visitors

def id_list(visitors_list):
    return { int(v["id"]) for v in visitors_list }


def add_visitor(visitors_list):
    print("\n--- Registering Visitor ---\n")

    id_value = int(input("ID: "))
    name = input("Name: ")
    species = input("Species: ")
    status = input("Status: ")

    visitor = {
        "id": id_value,
        "name": name,
        "species": species,
        "status": status
    }

    visitors_list.append(visitor)
    save_visitors_csv(visitors_list)
    save_visitors_json(visitors_list)

    return visitors_list


def save_visitors_csv(visitors):
    with open("visitors.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "species", "status"])
        writer.writeheader()
        writer.writerows(visitors)


def save_visitors_json(visitors):
    with open("visitors.json", "w", encoding="utf-8") as file:
        json.dump(visitors, file, indent=4, ensure_ascii=False)