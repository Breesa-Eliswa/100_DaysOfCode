#A program to generate random password
import string
import random 
characters = list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generate_password():

    password_length=int(input("How long would you like your password to be ? : "))
    #random.shuffle(characters)
    password =[]

    for x in range(password_length):
        #password.append(random.choice(characters))
        #random.shuffle(password)
        password =''.join(random.choice(characters))
        print(password,end='')

option = input("Do you want to generate a password type yes or no: ")
if option=="yes":
    generate_password()
elif option=="no":
    print("Program ended")
    quit()
else:
    print("Invalid choice , please enter yes or no")
    quit()



