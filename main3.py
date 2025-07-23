import numpy as np

die_sides = int(input("enter the number of sides (6/12) :"))
die = range(1, die_sides)

num_rolls = int(input("Enter number of times you want to roll the dice : * "))

result = np.random.choice(die, size = num_rolls, replace = True)
print(result)