def int_entry(message, min=None, max=None):

    flag = False
    while not flag:
        try:
            value = int(input(message).strip())
            if min is not None and value < min or max is not None and value > max:
                raise ValueError
            return value
        except ValueError:
            print("\nWrong Entry. Try again\n")


def str_entry(message):

    flag = False
    while not flag:
        value = input(message)
        if not value:
            print("The field cannot be empty \n")
            continue
        if not all(c.isalnum() or c.isspace() for c in value):
            print("The field must include only letters or numbers\n")
            continue
        break
    return value.lower()

# def yes_no(decision):

#     flag = False
#     while not flag:
#         if not decision:
#             print("\nChoose an option \n")
#             return
#         if not all(decision.lower()=="y" or decision.lower()=="n" or c.isdigit() for c in decision):
#             print("\nInvalid option. Try Again\n")
#             return
#         break
#     return decision.lower()
