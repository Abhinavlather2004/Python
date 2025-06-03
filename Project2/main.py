
import random
n = random.randint(1, 100)
a=0
guesses = 0
while (a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if a == n and guesses == 1:
        print("Wow! You guessed it on the first try!")
    elif a == n:
        print(f"Congratulations! You guessed the number {n} in {guesses} tries.")
    elif a < n:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

