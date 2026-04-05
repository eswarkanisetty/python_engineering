print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill =0

if size.lower() == 's' :
    bill = 15
elif size.lower() == 'm' :
    bill = 20
else :
    bill = 25

if pepperoni.lower() == 'y' :
    if size.lower() == 's' :
        bill+=2
    else :
        bill+=3
else :
    bill

if extra_cheese.lower() == 'y':
    bill += 1
    print(f" Your Final Bill is  : ${bill}")

else:
    print(f" Your Final Bill is  : ${bill}")