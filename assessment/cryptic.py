from datetime import datetime
import sys

current_time =datetime.now().strftime("%H:%M")
current_date=datetime.now()

#Open
def init():
    is_valid_option_selected = False 
    print(f"======Welcome to the Cipher generator======\nTime is {current_time} on {current_date}\nWhat would you like to do? ")
    print("1. Covert cipher code\n2. Logout")

    while is_valid_option_selected == False:
        proceed=int(input("choose option 1 or option2 above: "))

        if proceed == 1:
            is_valid_option_selected == True
            cipher =int(input("Which operation would you like to perform? 1. Encryption 2. Decryption: "))
            if cipher == 1:
                encrypt()
                break
            
            elif cipher == 2:
                decrypt()
                break

        elif proceed == 2:
            is_valid_option_selected == True
            exit()
            
        else:
            is_valid_option_selected == False
            print("Invalid option selected, ensure you pick between Y/N")


#encryption
def encrypt(): #pass shift count and text to encrypt as parameters...
    encryption=""
    text=input("Enter the character you want to encrypt: ")
    key=int(input("How many times do you want to shift the characters? "))
    for x in text:
        if x.islower():
            index = ord(x) - ord("a")
            new_index=(index + key)%26 #casear formula to perform the shift
            new_unicode=new_index + ord("a")
            new_char=chr(new_unicode)

            if text == "":
                print("")
            else: 
                encryption+=new_char

        else:
            encryption+=x
    print (encryption)
    new_operation()


#to continue with existing operation
def new_operation():
    option=input("Would you like to continue? Y/N: ")
    if option == "Y":
        init()
    elif option == "N":
        exit()
    else: 
        print("Invalid input, try again")
        new_operation()
        

#decryption
def decrypt():
    decryption=""
    text=input("Enter the encrypted character you want to decrypt: ")
    decode_key=int(input("How many times do you want to shift the encoded characters? "))
    for x in text:
        if x.islower():
            index=ord(x)-ord("a")
            new_index = (index - decode_key)%26
            new_unicode=new_index + ord("a")
            new_char=chr(new_unicode)

            decryption+=new_char

        else:
            decryption+=x
    print (decryption)
    new_operation()


#logout...
def exit():
    sys.exit(1)

#initialize operation.
init()