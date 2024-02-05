from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the Master Password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key", 'wb') as key_file:
        key_file.write(key)
write_key()
'''

def add():
    name = input("Account's Name: ")
    pwd = input("Enter the Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + " || "+ fer.encrypt(pwd.encode()).decode() +'\n')

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("||")
            print("User:"+ user , "Password:"+fer.decrypt(passw.encode()).decode())


def what_action():
    while True:
        action = input('What you want to do now, add new passwords (add),view old passwords (view) or q to quit: ').lower()
        if action == 'q':
            break


        if action == 'add':
            add()
        elif action == 'view':
            view()
        else:
            print("Wrong action, Enter from the brackets")


while True:
    if master_pwd == 'Utkarsh':
        what_action()
    else: 
        print('Wrong Password')



