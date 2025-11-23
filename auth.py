def admin_login(admin,attempts=3):
    if attempts == 0:
        print("Too many failed attempts")
        return False
    
    # user = input("User ID: ")
    # passw = input("Password: ")

    user = 'leahMaria11'
    passw = 'kokito23'

    if user == admin['username'] and passw == admin['password']:
        print('\n - - ACCESS GRANTED - - \n')
        return True
    
    else:
        print('Invalid ID User or Password. Attempts left: ' + str(attempts-1))
        return admin_login(admin,attempts-1)