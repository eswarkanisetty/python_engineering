# Range Function with for loop

print(range(1,10))

for i in range(1,11,2):
    print(i)

# summing 100 nums
sum=0
for i in range(0,101):
    sum += i
print(sum)

# Fizz Buzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
