import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

play = True

while play:
    choice = input("Type encode to encrypt, type decode to decrypt").lower()
    message = input("Type your message").lower()
    shift_num = int(input("Type the shift number:"))
    en_message = ""
    de_message = ""
    if choice == 'encode':
        for i in message:
            en_pos = alphabet.index(i) + shift_num
            en_message += alphabet[en_pos%26]
        print(f"Here's the encoded result {en_message}")
    elif choice == 'decode':
        for i in message:
            en_pos = alphabet.index(i) - shift_num
            de_message += alphabet[en_pos%26]
        print(f"Here's the decoded result {de_message}")

    yes_no = input("Type 'yes' if you want to go again or Type 'no'").lower()

    if yes_no == 'yes':
        play = True
    else :
        play = False




