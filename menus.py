import utils
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def principal_menu():
    msg = ("\n===== GALACTIC LIBRARY KEEPER =====\n\n"
        "1. LOGIN 🔐\n"
        "2. EXIT ⛔\n\n"
        "Choose an option: ")

    option = utils.int_entry(msg,1,2)
    return option

def admin_menu():
    msg = ("\n===== ADMINISTRATORS MENU =====\n\n"
        "1. Visitors Module\n"
        "2. Artifacts Module\n"
        "3. Back:\n\n"
        "Choose an option: ")

    option = utils.int_entry(msg,1,3)
    return option

def visitors_menu():
    msg = ("\n===== VISITORS MODULE =====\n\n"
        "1. Visitor Registration\n"
        "2. Show Visitors\n"
        "3. Find Visitor\n"
        "4. Update Status\n"
        "5. Remove Visitor\n"
        "6. Stats\n"
        "7. Back\n\n"
        "Choose an option: ")

    option = utils.int_entry(msg,1,7)
    return option

def artifacts_menu():
    msg = ("\n===== ARTIFACTS MODULE =====\n\n"
        "1. Artifact Registration\n"
        "2. Show Artifacts\n"
        "3. Find Artifact\n"
        "4. Artifacts Clasification\n"
        "5. Remove Artifact\n"
        "6. Stats\n"
        "7. Back\n\n"
        "Choose an option: ")

    option = utils.int_entry(msg,1,7)
    return option

def visitors_stats():
    msg = ("\n===== STATISTICS MODULE =====\n\n"
        "1. Total Visitors\n"
        "2. Visitors per Species\n"
        "3. Active VS Retired Visitors\n"
        "4. Back\n"
        "Choose an option: ")

    option = utils.int_entry(msg,1,4)
    return option

def clasification_menu():
    pass

