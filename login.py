from time import sleep

def register():
    global username,password,secret_pin
    x = str(input("Enter username: "))
    y = str(input("Enter password(must be less than 8 character): "))
    z = int(input("Enter the pin(must be integer, 4 digit): "))
    username = x
    password = y
    secret_pin = z


    if (username,password,secret_pin == True):
        print("Registeration Successful !")
    else:
        print("Registeration Failed !")
        
    condition = input("Want to continue to login screen? (yes/no): ")
    if condition == 'yes':
        pass
    else:
        quit()
    sleep(3)
    


def login():
    uname = str(input("Enter your username: "))
    passw = str(input("Enter your password: "))
    s_pin = int(input("Enter your 4 digit pin: "))
    
    if uname == username and passw == password and s_pin == secret_pin:
        print("login successful")
    else:
        print("Invalid Information")
    
    

    