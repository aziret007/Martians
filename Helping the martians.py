
import random

locations = [random.randint(1, 10) for _ in range(3)]
weights = [random.randint(200, 300) for _ in range(3)]
total_weight = sum(weights)

print("The total weight of the boxes is:", total_weight)
print("Welcome! You need to find three boxes such that their total weight equals 713 kg.")
print("If you enter the wrong locations, the boxes will move to new locations.")

while True:
    try:
        guesses = [int(input(f"Enter location {i + 1}: ")) for i in range(3)]
    except ValueError:
        print("Please enter valid numbers!")
        continue

    if guesses == locations:
        print("You found all the boxes!")
        print(f"Box weights: {weights}")
        if sum(weights) == 713:
            print("Congratulations! The total weight of the boxes is 713 kg. You succeeded!")
            break
        else:
            print(f"The total weight of the boxes is {sum(weights)}, but it is not 713 kg. Try again!")
    else:
        print("Wrong locations. The boxes have moved to new locations!")
        locations = [random.randint(1, 10) for _ in range(3)]

print("Thank you for using the program. Good luck!")
