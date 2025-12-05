import storage
import auth
import utils
import artifacts
import visitors
from menus import clear, principal_menu, admin_menu, visitors_menu, artifacts_menu, artifacts_stats, visitors_stats

flag_menu = False
flag_login = False

admin_flag,admin = storage.load_file('admin_access.csv')

while not flag_menu:
    op = principal_menu()

    if op == 1:
        flag_menu = False
        flag_login = auth.admin_login(admin)

        if flag_login:flag_menu = True
    elif op ==2:
        flag_menu = True
        clear()
        print("\nExiting System")

while flag_login:
    clear()
    op = admin_menu()

    match op:
        case 1:
            clear()
            visitors_list = visitors.load_visitors()
            flag_visitors = False

            while not flag_visitors:
                clear()
                option = visitors_menu()

                match option:
                    case 1:
                        clear()
                        visitors_list = visitors.add_visitor(visitors_list)
                        print(input("\nPress enter to go back "))
                    case 2:
                        clear()
                        visitors.show_visitors(visitors_list)
                        print(input("\nPress enter to go back "))
                    case 3:
                        clear()
                        print("- - - FINDING VISITOR - - -\n")
                        visitor_ID = utils.int_entry("Visitor ID: ",0,999)
                        found_ID,x = visitors.find_visitor(visitor_ID, visitors_list)
                        if found_ID is not None:
                            print("\n- - - - - - Search result - - - - - -\n") 
                            print(f"Visitor: {found_ID['name'].capitalize()} | Species: {found_ID['species'].capitalize()} | Status: {found_ID['status'].capitalize()}")
                
                        else:
                            print("\nNo visitor found\n")
                        print(input("\nPress enter to go back "))
                    case 4:
                        clear()
                        print("\n- - - - - - - UPDATING STATUS - - - - - - -")
                        visitors.show_visitors(visitors_list)
                        print("\n")
                        visitor_ID = utils.int_entry("Visitor ID: ",0,999)
                        found_ID,x = visitors.find_visitor(visitor_ID, visitors_list)

                        if found_ID is not None:
                            visitors_list = visitors.update_visitor(visitor_ID, visitors_list)
                            print(input("\nPress enter to go back "))
                        
                        else:
                            print("\nNo Visitor found\n")
                            print(input("\nPress enter to go back "))
                    case 5:
                        clear()
                        visitors.show_visitors(visitors_list)
                        print("\n")
                        visitor = utils.int_entry("Visitor ID: ")
                        visitors_list = visitors.remove_visitor(visitor,visitors_list)
                        print(input("\nPress enter to go back "))
                        clear()
                    case 6:
                        clear()
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
                                    clear()
                                    flag_stats = True

                    case 7:
                        clear()
                        flag_visitors = True
                        flag_menu = False
        case 2:
            art_list = artifacts.load_artifacts()
            flag_arts = False

            while not flag_arts:
                clear()
                option = artifacts_menu()

                match option:
                    case 1:
                        clear()
                        art_list = artifacts.add_artifact(art_list)
                    case 2:
                        clear()
                        artifacts.show_artifacts(art_list)
                        print(input("\nPress enter to go back "))
                        clear()
                    case 3:
                        clear()
                        print("- - - FINDING ARTIFACT - - -\n")
                        artifact_ID = utils.int_entry("Artifact ID: ",0,999)
                        found_ID,x = artifacts.find_artifact(artifact_ID, art_list)
                        if found_ID is not None:
                            print("\n- - - - - - Search result - - - - - -\n") 
                            print(f"Artifact ID: {found_ID['id']} | Description: {found_ID['description'].capitalize()} | Rarity: {found_ID['rarity'].capitalize()} | Status: {found_ID['status'].capitalize()}")
                    
                        else:
                            print("\nNo artifact found\n")
                            print(input("\nPress enter to go back "))
                        clear()
                    case 4:
                        clear()
                        artifacts.art_clasification(art_list,rarity="low")
                        artifacts.art_clasification(art_list, rarity="high")
                        artifacts.art_clasification(art_list,rarity='prohibid') 
                        print(input("\nPress enter to go back "))
                        clear()            
                    case 5:
                        clear()
                        artifacts.show_artifacts(art_list)
                        print("\n")
                        artifact = utils.int_entry("Artifact ID: ")
                        art_list = artifacts.remove_artifact(artifact,art_list)
                        print(input("\nPress enter to go back "))
                        clear()
                    case 6:
                        flag_stats_art = False

                        while not flag_stats_art:
                            clear()
                            option = artifacts_stats()

                            match option:
                                case 1:
                                    clear()
                                    print(f'{"The total number of artifacts registered is:"} {len(art_list)}')
                                    print(input("\nPress enter to go back "))
                                    clear()

                                case 2:
                                    clear()
                                    print(artifacts.artifacts_rarity(art_list))
                                    print(input("\nPress enter to go back "))
                                    clear()
                                    #falt aponerlo lindo

                                case 3:
                                    clear()
                                    print(artifacts.artifacts_status(art_list))
                                    print(input("\nPress enter to go back "))
                                    clear()
                                    #falt aponerlo lindo

                                case 4:
                                    clear()
                                    flag_stats_art = True
                                    flag_menu = False
                    case 7:
                        clear()
                        flag_arts = True
                        flag_menu = False
        case 3:
            clear()
            flag_menu = True
            flag_login = False
            print("\nThanks for using the Galactic System")
    
