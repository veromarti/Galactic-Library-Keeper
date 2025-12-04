import storage
import auth
import utils
import artifacts
import visitors
from menus import clear, principal_menu, admin_menu, visitors_menu, artifacts_menu, clasification_menu, visitors_stats

flag_menu = False

# user='leahMaria11'
# password='kokito23'

admin_flag,admin = storage.load_file('admin_access.csv')

# print(admin)
# print(admin_flag)

# auth.admin_login(admin)

while not flag_menu:
    op = principal_menu()

    if op == 1:
        flag_menu = False
        flag_login = auth.admin_login(admin)

    if flag_login:flag_menu = True

while flag_login:
    op = admin_menu()

    match op:
        case 1:
            visitors_list = visitors.load_visitors()
            print(visitors_list)
            
            flag_visitors = False

            while not flag_visitors:
                option = visitors_menu()

                match option:
                    case 1:
                        visitors_list = visitors.add_visitor(visitors_list)
                        print(visitors_list)
                    case 2:
                        visitors.show_visitors()
                        print(input("\nPress enter to go back "))
                        #falta ponerlo lindo
                    case 3:
                        print("- - - Finding Visitor - - -\n")
                        visitor_ID = utils.int_entry("Visitor ID: ",0,999)
                        found_ID,x = visitors.find_visitor(visitor_ID, visitors_list)
                        if found_ID is not None:
                            print("- - - - - - Search result - - - - - -\n") 
                            print(f"Visitor: {found_ID['name'].capitalize()} | Species: {found_ID['species'].capitalize()} | Status: {found_ID['status'].capitalize()}")
                
                        else:
                            print("\nNo visitor found\n")
                        print(input("\nPress enter to go back "))

                    case 4:
                        print("\n- - - - - - - UPDATING STATUS - - - - - - -")
                        visitors.show_visitors()
                        print("\n")
                        visitor_ID = utils.int_entry("Visitor ID: ",0,999)
                        found_ID,x = visitors.find_visitor(visitor_ID, visitors_list)

                        if found_ID is not None:
                            visitors_list = visitors.update_visitor(visitor_ID, visitors_list)
                            print(input("\nPress enter to go back "))
                        
                        else:
                            print("\nNo Visitor found\n")
                            print(input("\nPress enter to go back "))
                            
                        # pass
                        # clasification_menu()
                        
                        # artifacts.art_clasification(art_list,rarity='prohibid')
                        
                        # artifacts.art_clasification(art_list,rarity="low", status="stored")
                    case 5:
                        clear()
                        visitors.show_visitors()
                        print("\n")
                        visitor = utils.int_entry("Visitor ID: ")
                        visitors_list = visitors.remove_visitor(visitor,visitors_list)
                        print(input("\nPress enter to go back "))
                        clear()
                        
                    case 6:
                        flag_stats = False

                        while not flag_stats:
                            option = visitors_stats()

                            match option:
                                case 1:
                                    clear()
                                    print(f'{"The total number of visitors is:"} {len(visitors.id_list(visitors_list))}')
                                    print(input("\nPress enter to go back "))
                                    clear()

                                case 2:
                                    clear()
                                    print(visitors.visitors_species(visitors_list))
                                    print(input("\nPress enter to go back "))
                                    clear()
                                    #falt aponerlo lindo

                                case 3:
                                    clear()
                                    print(visitors.filter_status(visitors_list))
                                    print(input("\nPress enter to go back "))
                                    clear()
                                    #falt aponerlo lindo

                                case 4:
                                    flag_stats = True

                    case 7:
                        flag_visitors = True
        case 2:
            art_list = artifacts.load_artifacts()
            print(art_list)
            option = artifacts_menu()

            match option:
                case 1:
                    art_list = artifacts.add_artifact(art_list)
                    print(art_list)
                case 2:
                    artifacts.show_artifacts(art_list)
                    print(input("\nPress enter to go back "))
                case 3:
                    print(artifacts.find_artifact(123,art_list))
                case 4:
                    artifacts.art_clasification(art_list,rarity="low")
                    artifacts.art_clasification(art_list, rarity="high")
                    artifacts.art_clasification(art_list,rarity='prohibid')             
                case 5:
                    pass
                case 6:
                    clear()
                    artifacts.show_artifacts(art_list)
                    print("\n")
                    art = utils.int_entry("Artifact ID: ")
                    art_list = visitors.remove_visitor(art,art_list)
                    print(input("\nPress enter to go back "))
                    clear()
                case 7:
                    
                    pass
        case 3:
            clear()
            flag_menu = True
            print("\nThanks for using the Galactic System")
    
