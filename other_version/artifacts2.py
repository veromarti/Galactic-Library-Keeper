import csv
import json

def load_artifacts():
    artifacts = []
    try:
        with open("artifacts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                artifacts.append(row)
    except FileNotFoundError:
        pass
    return artifacts


def add_artifact(artifacts_list):
    print("\n--- Registering Artifact ---\n")

    code = input("Code: ")
    description = input("Description: ")
    rarity = input("Rarity (Low/Medium/High/Forbidden): ")
    status = input("Status (Stored/In Study/Destroyed): ")

    artifact = {
        "id": code,
        "description": description,
        "rarity": rarity,
        "status": status
    }

    artifacts_list.append(artifact)
    save_artifacts_csv(artifacts_list)
    #save_artifacts_json(artifacts_list)

    return artifacts_list

def list_artifacts(artifacts_list):
    print("\n--- Artifact List ---\n")
    for art in artifacts_list:
        print((
            art["id"],
            art["description"],
            art["rarity"],
            art["status"]
        ))


def save_artifacts_csv(artifacts):
    with open("artifacts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=['id','description','rarity','status'])
        writer.writeheader()
        writer.writerows(artifacts)

# def save_artifacts_json(artifacts):
#     with open("artifacts.json", "w", encoding="utf-8") as file:
#         json.dump(artifacts, file, indent=4, ensure_ascii=False)
