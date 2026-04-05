print("Welcome to the rollercoaster !!")
height = int(input("Enter your height"))
bill =0

if height > 120 :
    print("Enter the rollercoaster !!")
    age = int(input("Enter your age \n"))
    if 18 <= age < 45 :
        bill = 12
    elif 12 < age < 18 :
        bill = 7
    elif age >= 45 and  age <= 55 :
        bill =0
    else :
        bill = 5
else :
    print("you are not enough taller !!")

photo = input("Do you want photo ? : y / n ")

if photo.lower() == 'y' :
    bill += 3
    print(f"Your Total price is : {bill}")