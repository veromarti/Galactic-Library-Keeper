import storage
import auth
import validation
import artifacts
import visitors
from utils import clear,principal_menu,admin_menu,visitors_menu,artifacts_menu,clasification_menu

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
            option = visitors_menu()

            match option:
                case 1:
                    visitors_list = visitors.add_visitor(visitors_list)
                    #art_list = artifacts.add_artifact(art_list)
                    print(visitors_list)
                case 2:
                    
                    visitors.listar_visitantes()
                case 3:
                    pass
                    print(artifacts.find_artifact(123,art_list))
                case 4:
                    pass
                    clasification_menu()
                    
                    artifacts.art_clasification(art_list,rarity='prohibid')
                    
                    artifacts.art_clasification(art_list,rarity="low", status="stored")
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
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
                case 3:
                    print(artifacts.find_artifact(123,art_list))
                case 4:
                    clasification_menu()
                    
                    artifacts.art_clasification(art_list,rarity='prohibid')
                    
                    artifacts.art_clasification(art_list,rarity="low", status="stored")
                
                    artifacts.art_clasification(art_list, "rarity=high", "status=stored")              
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
        case 3:
            pass
    
