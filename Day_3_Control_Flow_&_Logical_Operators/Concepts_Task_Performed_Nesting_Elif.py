print("Welcome to the rollercoaster !!")
height = int(input("Enter Your Height ? : \n"))
price = 0

if (height >= 120) :
    print("Enter to the Rollercoaster !!")
    age = int(input("Enter your age \n"))
    if  18 < age < 50 :
        print(f"Your Ticket Price is : {12}")
    elif 12 < age <= 18 :
        print(f"Your Ticket Price is : {7}")
    elif age < 12 :
        print(f"Your Ticket Price is : {5}")
    else :
        print(f"Your Ticket Price is : {0}")
else :
    print("Sorry you are not tall enough for thr ride")