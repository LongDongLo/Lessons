counter = 0
guess = 0
guesses = 0

while counter < 7 and guess != 69:
    guess = int(input("Guess a number from 1 to 100. You have 7 guesses: "))
    if guess != 69:
        print("Incorrect")
    counter = counter + 1
    guesses = guesses + guess
if counter == 7:
    print("You failed. Too many guesses.")
else:
    print("Great job! You guessed the number.")
if guess == 69:
  guesses = guesses - guess
print("Your wrong answers added together equal " + str(guesses) + ".")
if guesses > 100:
    print("What a dweeb")

