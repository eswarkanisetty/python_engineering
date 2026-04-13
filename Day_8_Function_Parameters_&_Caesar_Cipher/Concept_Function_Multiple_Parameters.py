def gret_with(name, location):
    print(f"{name} is at {location}")

gret_with(name="Eswar", location="NJ")

# Love Score
def calculate_love_score(name1, name2):
    a = "TRUE"
    b = "LOVE"
    t1 = 0
    t2 = 0
    t = 0
    l1 = 0
    l2 = 0
    l = 0

    for i in a.lower():
        for y in name1.lower():
            if i==y:
                t1 += 1
        for z in name2.lower():
            if i==z:
                t2 += 1
    t = t1 + t2
    for w in b.lower():
        for y in name1.lower():
            if w==y:
                l1 += 1
        for z in name2.lower():
            if w==z:
                l2 += 1
    l = l1 + l2

    print(f"Love Score = {t}{l}")

calculate_love_score("Angela Yu", "Jack Bauer")