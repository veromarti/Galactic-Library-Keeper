def admin_login(admin,attempts=3):
    if attempts == 0:
        print("Too many failed attempts")
        return False
    

    user = 'leahMaria11'
    passw = 'kokito23'

    if admin['role'] == 'SUPERADMIN':
        # user = input("User ID: ")
        # passw = input("Password: ")
        if user == admin['username'] and passw == admin['password']:
            print('\n - - ACCESS GRANTED - - \n')
            return True
    
        else:
            print('Invalid ID User or Password. Attempts left: ' + str(attempts-1))
            return admin_login(admin,attempts-1)
    else:
        print('\nSUPERADMIN was not detected\n')
        return admin_login(admin,attempts-1)