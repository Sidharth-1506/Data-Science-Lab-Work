import random

number = random.randint(1, 100)

attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You have", attempts, "attempts")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You guessed the number!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0 and guess != number:
    print("Game Over! The number was:", number)
