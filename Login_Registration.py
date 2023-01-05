title = '------Welcome------'
print(title.center(70))
choose = 'Press 1 for Login or Press 0 for Register\n'
print(choose.center(70))
import re
user = int(input('Select Your Option:'))
f = open('userdetails.txt','a')          
if user == 0:
    print('REGISTRATION'.center(70))
    while True:
        email = input('Enter Your Email ID:')
        pattern = '[(a-zA-Z)][(a-zA-Z0-9_)]+[@][(a-z)]+[.][com]{3}'
        matches = re.fullmatch(pattern,email)
        if matches == None:
            print('Invalid Email ID Format')
            print('First Letter should not be a DIGIT or a SPECIAL CHARACTER')
            print('Example Format:jonesarieh@gmail.com')
            continue
        elif matches != None:
            break
    while True:
        password = input('Enter Your Password:')
        pattern1 = '^(?=.{5,16}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$'
        matches1 = re.fullmatch(pattern1, password)  
        if matches1 == None:
            print('''
                  Must have Minimum 
                  One Special Character, 
                  One digit, One Uppercase, 
                  One Lowercase
                  Must Contain 5 to 16 Characters
                  ''') 
            continue
        elif matches1 != None:
            print('Registered Successfully'.center(70))                  
            break    
    # File Handling
    f = open('userdetails.txt','a')
    f.write(email + '\n')
    f.write(password + '\n')
    f.close()

elif user == 1:
    print('lOGIN'.center(70))
    email = input('Enter Your Email ID:')   
    password = input('Enter Your Password:')
    with open('userdetails.txt') as f:
        file = f.readlines()
        if len(file) == 0:
            print('User Credentials Not Found, Please Register'.center(70))
    for i in file:
        if email in i:
            x = file.index(i)
            x = x+1
            # print(x)
            # print(i)
            if password in file[x]:
                print("'Login Successful'".center(70))
                break
            elif password not in file[x]:
                print("'Password not Match'".center(70))
                FP = int(input('Press 1 if you forget password or Press 0 to exit:'))
                # print(FP)
                if FP == 1:
                    print('Your Password is',file[x])
                elif FP == 0:
                    break 
                break
            break
        elif email not in i and len(file)-1 == file.index(i):
            print('User Credentials Not Found, Please Register'.center(70)) 
                         
else:
    print('Invalid input')