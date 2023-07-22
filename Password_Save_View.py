''' We often gets baffled with the passwords of various accounts or worse forgets it right..?
    So this is  a python program to save your passwords.Also do remember to amend your passwords 
    whenevr you change it by using the add option. The passwords of the various accounts could be seen by 
    entering the view option'''


def add():
    name= input("Account name: ")
    pwd =input("Password: ")
    with open('password.txt','a') as f:  #Create a text file named password
        f.write(name + "|" + pwd +"\n")

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            
            user,passw=data.split("|")
            print("User: ",user,"| Password: ",passw)

while True:
    mode = input("Would you like to add a new password or view the already  existing password (add/view) or press q to quit \n")
    if mode=="q":
        break
    if mode=="add":
        add()
    elif mode=="view":
        view()
    else:
        print("Invalid Entry")