import random
print("Infinite Dice")
def rollDice(sides):
  roll = random.randint(1, sides)
  print("You rolled",roll)
  repeat = input("Roll again? ")
  if repeat == "yes" or repeat == "y" or repeat == "Yes" or repeat == "YES" or repeat == "yES":
    rollDice(sides)
  else:
    print("Bye!")

sides = int(input("How many sides? "))
rollDice(sides)