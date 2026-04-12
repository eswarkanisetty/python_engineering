#Functions
def my_function():
  print("Hello")

my_function()


#Reeborg's Game
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json#

# Draw Square
def turn_around():
    for i in range(0, 2):
        turn_left()


def turn_right():
    for i in range(0, 3):
        turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_around()

# Hurdle 1
def turn_right():
    for i in range(0, 3):
        turn_left()


def one_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for i in range(0, 6):
    one_jump()

# Hurdle 1 using while loop
No_Of_hurdles = 6

while No_Of_hurdles >0:
    one_jump()
    No_Of_hurdles -=1

# Hurdle 2 using while loop with not condition
while not at_goal():
    one_jump()

# Hurdle 3 Using While and If Loops
def inst_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        inst_jump()
    else:
        move()


# Hurdle 4 using while, if loops

def turn_around():
    for i in range(0, 2):
        turn_left()


def turn_right():
    for i in range(0, 3):
        turn_left()


def one_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def inst_jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        inst_jump()
    else:
        move()

# Maze using While, if/elif loops :

def turn_around():
    for i in range(0, 2):
        turn_left()


def turn_right():
    for i in range(0, 3):
        turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()





