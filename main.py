import random


# print(help(random))

low = 1

high = 100

guesses = 0

number = random.randint(low, high)


# options = ("rock", "paper", "scissors")

# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# # number = random.random() float number between 0 and 1 
# options = random.choice(options)

# random.shuffle(cards)

# print(cards)

# print(options)

# print(number)


while True:
    guess = int(input(f"Enter a number between {low} and {high} "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print("you guessed right ")
        break

print(f"number of guesses: {guesses}")