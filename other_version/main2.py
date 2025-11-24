import visitors3
import artifacts2

visitors_list = visitors3.load_visitors()
artifacts_list = artifacts2.load_artifacts()

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def main_menu():
    while True:
        print("""
==========================
  GALACTIC LIBRARY KEEPER
==========================
1. Register Visitor
2. List Visitors
3. Register Artifact
4. List Artifacts
5. Exit
==========================
""")

        option = read_int("Select an option: ")

        if option == 1:
            visitors3.add_visitor(visitors_list)

        elif option == 2:
            print("\n--- Visitors List ---\n")
            for v in visitors_list:
                print((v["id"], v["name"], v["species"], v["status"]))

        elif option == 3:
            artifacts2.add_artifact(artifacts_list)

        elif option == 4:
            artifacts2.list_artifacts(artifacts_list)

        elif option == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
