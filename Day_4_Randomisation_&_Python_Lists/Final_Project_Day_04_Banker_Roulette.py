import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
enemies = ["Alice", "Bob1", "Charlie", "David", "Emanuel"]

# Using Choice
print(random.choice(friends))

# Using randint
rn_int = random.randint(0,4)
print(friends[rn_int])
