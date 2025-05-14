import random

#
score = 0
rolls = []

#
print("welcome bozos")
print("we're playing a game")

#
while score < 50:
    input("roll the die by pressing enter")
    die = random.randint(1, 6)
    die2 = random.randint(1, 6)
    score += die 
    rolls.append(die) 

    print(die)
    print(die2)

#
print("yip yip hooray")

#
show_history = input("Do you want to see your roll history? (yes/no): ").strip().lower()

#
if show_history == 'yes':
   print("History of your rolls:")
   for index, roll in enumerate(rolls, start=1):
       print(f"Roll {index}: {roll:}")
else:
    print("Goodbye Bozos")