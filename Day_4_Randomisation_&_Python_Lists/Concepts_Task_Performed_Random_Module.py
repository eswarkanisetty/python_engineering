import random
import My_Module

rand_int = random.randint(1,10)
print(rand_int)

print(My_Module.rand_int1)

#random_random --- float btw 0-1
randm_0_to_1 = random.random()
print(randm_0_to_1)

randm_0_to_10 = random.random() * 10
print(randm_0_to_10)

#random_random ---random float btw the range
rand_uni = random.uniform(1,10)
print(rand_uni)

#Random_Choice  --- random
coin = ['Heads', 'Tails']
random_choc = random.choice(coin)
print(random_choc)

rand_coin = random.randint(0,1)
if rand_coin == 0:
    print("Heads")
else :
    print("Tails")