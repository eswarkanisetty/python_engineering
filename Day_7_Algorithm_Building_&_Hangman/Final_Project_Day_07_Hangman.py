import random
import hangman_words
import hangman_art

computer = random.choice(hangman_words.word_list)
print(computer)
place_holder = []
com_list=[]
chances = 7
hang_stage = len(hangman_art.stages) - 1
game = False

for i in computer:
    com_list +=i
print(com_list)

for i in range(len(com_list)):
    place_holder += "_"
print(place_holder)

while not game:
    print(f"you have {chances} chances left")
    user = input("guess a letter !!!").lower()
    for i in range(len(com_list)) :
        if com_list[i] == user:
            place_holder[i] = user
            if com_list == place_holder:
                game = True
                print("Game Over You have Won")
    if user not in com_list :
        print(hangman_art.stages[hang_stage])
        hang_stage -=1
        chances -=1
        if chances == 0:
            game = True
            print("Game Over You have Lost and Hanged")
    print(place_holder)




