secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess the number (1-20): "))
    attempts = attempts + 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed the number!")
        print(f"You got it in {attempts} tries!")
        break
