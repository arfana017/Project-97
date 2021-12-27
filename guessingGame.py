import random

print("Number Guessing Game")

r = random.randint(1,9)
print(r)
g = input("Guess a number (between 0 and 10): ")

count = 1

while count < 5:
    if int(g) < r:
        print("Your guess was too low; try a higher number!")
        g = input("Guess again: ")
        count += 1
        print("Count: " + str(count))
    
    if int(g) > r:
        print("Your guess was too high; try a lower number!")
        g = input("Guess again: ")
        count += 1
        print("Count: " + str(count))
    
    if int(g) == r:
        print("That was the correct number, congrats!!")
        break

if count >= 5 and int(g) != r:
        print("You've run out of tries, the number was", str(r))
