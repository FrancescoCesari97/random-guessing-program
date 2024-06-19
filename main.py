import random


# print(help(random))

# low = 1

# high = 100

# guesses = 0

# number = random.randint(low, high)


# options = ("rock", "paper", "scissors")

# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# # number = random.random() float number between 0 and 1 
# options = random.choice(options)

# random.shuffle(cards)

# print(cards)

# print(options)

# print(number)


# while True:
#     guess = int(input(f"Enter a number between {low} and {high} "))
#     guesses += 1

#     if guess < number:
#         print(f"{guess} is too low")
#     elif guess > number:
#         print(f"{guess} is too high")
#     else:
#         print("you guessed right ")
#         break

# print(f"number of guesses: {guesses}")


##### ROCK PAPER SCISSORS


options = ("rock", "paper", "scissors")

player = None 

computer = random.choice(options)

player = input("Enter a choice: ").lower()

while player not in options:
    print("Enter a valid choice (rock, paper, scissors)")
    player = input("Enter a choice: ").lower()

print(f"Player chose: {player}")
print(f"Computer chose: {computer}")



if player == computer:
    print("it's a tie!")
elif player == "rock" and computer == "scissors":
    print ("player win!")
elif player == "paper" and computer == "rock":
    print("player win!")
elif player == "scissors" and computer == "paper":
    print("player win")
else:
    print("computer won!")
   
    