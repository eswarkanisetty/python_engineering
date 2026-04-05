print("Welcome to the roller coaster !!")
height= int(input("Enter your height ? : \n"))

if (height >= 120) :
    print("Enter the Rollercoaster !!")
    age = int(input("Enter your age \n"))
    ticket_price = 0

    if 18<=age<50 :
        print(f"Your ticket price is {12}")
        ticket_price = 12
    elif 12<=age<18:
        print(f"Your ticket price is {7}")
        ticket_price = 7
    elif age<12:
        print(f"Your ticket price is {5}")
        ticket_price = 5
    else :
        print(f"Your ticket price is {0}")
        ticket_price =0
else :
    print("your are not tall enough for the ride")

photo = input("You want a photo ? yes or no : \n")
photo_price =3

if photo.lower() == 'yes' :
    print(f"Your final ticket price is : {ticket_price + photo_price}")
else :
    print(f"Your final ticket price is : {ticket_price}")

