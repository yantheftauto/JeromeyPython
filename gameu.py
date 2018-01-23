# "Downloads" the entire Python module "random", which includes the function "randint"
import random

# Randomly generates a number between two numbers
rng_goblin = random.randint(200,1000)
rng_player = random.randint(0,15)
rng_weapon = random.randint(1,100)

# If random number is between 0 and 50, the goblin has a club
if 0 < rng_weapon and rng_weapon <= 50:
    weapon = "club"
# Else if its between 51 and 100, it has a freakin' battle axe
elif 51 < rng_weapon and rng_weapon <= 100:
    weapon = "battle axe"

# Uncomment the below print statement to see what number is being generated # (Tip: Click the line you want to comment or uncomment, and ctrl+/)
print(rng_weapon)

print("A goblin swings his {} at you!" .format(weapon))
print("He deals {0} damage! You lose {1} health! \n" .format(rng_goblin, rng_goblin))
print("You reel backwards but manage to recover yourself. \
\n\nUnsheathing your meager gathering knife, you swing maniacally and deal back {} damage! \n" .format(rng_player))

# These are variables that hold specific words, phrases, or sentences called "strings"
choice_a = "continue swinging what amounts to a butter knife at the goblin"
choice_b = "fuck everything and run"
choice_c = "scream like a little bitch and hope the goblin disintegrates"

print("You essentially did jackshit to it. Do you: \ \n a) {0}? \
\n b) {1}? \
\n c) {2}? \n" .format(choice_a, choice_b, choice_c))

# Try entering something other than a, b, or c, and see what happens
while(True):
    choice = input("You choose: ")
    if choice == "a":
        action = choice_a
        break
    elif choice == "b":
        action = choice_b
        break
    elif choice == "c":
        action = choice_c
        break
    else:
        print("You did not enter a valid choice.")
        print("\nYou have decided to {}. You can probably guess what happens next." .format(action))
