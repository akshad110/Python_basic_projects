letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
          ]


def encryption(plain_message,shift_key):
    ciper_text =""
    for char in plain_message:
        if char in letters:
           position = letters.index(char)
           new_position = (position+shift_key)%26
           ciper_text += letters[new_position]
        else:
            ciper_text += char
    print(f"The encrpyted cipher text is: {ciper_text}")

def decryption(cipher_text,shift_key):
    plain_message =""
    for char in cipher_text:
        if char in letters:
           position = letters.index(char)
           new_position = (position-shift_key)%26
           plain_message += letters[new_position]
        else:
            plain_message += char
    print(f"The decrpyted cipher text is: {plain_message}")

flag = False
while not flag:
    en_dn = input("Type encrypt for encryption, Type decrypt for decryption: \n")
    message = input("Enter your Message: \n").lower()
    shift = int(input("Type shift number: \n"))

    if en_dn == "encrypt":
        encryption(plain_message=message, shift_key=shift)
    elif en_dn == "decrypt":
        decryption(message, shift)
    play_again = input("Do you want to play again 'yes' or 'no': ")
    if play_again == 'no':
        flag = True
        print("Good bye!!!")