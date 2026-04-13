def greet():
    print("Hi")
    print("Hii")
    print("Hiii")

greet()

def greet_with_name(name):
    print(f"Hi{" "}{name}")

greet_with_name("Eswar")


def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52

    return weeks_left


print(f"you have {life_in_weeks(56)} weeks left.")