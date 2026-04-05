print("Welcome to the Tip Calculator !!")
total_bill = int(input("What was the total bill ? : \n"))
tip = int(input("How much Tip you would like to give ? 10,12 or 15 : \n"))
split = int(input("How many people to Split the Bill ? : \n"))
pay = (total_bill + (total_bill * (tip / 100))) / split
print(f"Each Person Should Pay : ${pay}")
