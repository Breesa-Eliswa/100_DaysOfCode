
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(text,shift,cipher_direction):
    end_text=''
    if direction=='decode':
            shift*=-1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position=position+shift
            new_letter=alphabet[new_position]
            end_text+=new_letter
        else:
            end_text+=char
    print(f"The {direction}ed text is {end_text}.")
        
while True:
    direction = input("Type encode to encrypt , type decode to decrypt \n ")
    message = input("Type your message \t").lower()
    shift_amount= int(input("Enter the number of places to be shifted: \t "))
    shift_amount = shift_amount%26

    caesar(text=message,shift=shift_amount,cipher_direction=direction)
    result=input("Type yes if wanna continue or no to exit the program \t").lower()
    if result=="no":
        print("Good Bye!!")
        exit()
    