import csv

def load_file(csv_file):

    admin = {}
    admin_header = ['username','password','role']

    try:
        with open(csv_file, newline = "", encoding = "utf-8") as file:
            reader = csv.reader(file)
            current_header = next(reader)
            
            if current_header == admin_header:
                is_admin = True

            else:is_admin = False

            for num, row in enumerate(reader, start=2):

                username, password, role = row

                admin={
                    'username':username,
                    'password':password,
                    'role':role
                }
    
    except UnicodeDecodeError:
        print("Wrong file encoding")
    
    except FileNotFoundError:
        print(f"File not found {csv_file}")
    
    except Exception as error:
        print(f"Unexpected error: {error}")
    
    return is_admin,admin