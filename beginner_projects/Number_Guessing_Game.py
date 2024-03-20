# This game takes input from the user (lower bound and upper bound), and generate random number btw range.
# the program calculates minimum number of guesses to play
# if user input the guess greater than random number, console will print "Guess is too high"
# if user input the guess smaller than random number, console will print "Guess is too small"
# if user input matches the random number, it prints "Congratulations, You Dit It"

import random,math

# Taking Input (Lower and Upper bound)
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Calculating Number of Guesses
min_guess = round(math.log(upper - lower + 1,2))
print("\n \t You Have Only ", min_guess , "Number Of Guesses \n \t")

# Generating Random Number
number = random.randint(lower,upper)

# Initilizing Counter variable
count = 0

# Initilizing loop
while count <= min_guess:
    count += 1
    guess = int(input("Enter your guess: "))
    if guess == min_guess:
        print("\n \t Congragulations, You Did It \n \t")
    elif guess < min_guess:
        print("Your Guess is too small")
    elif guess > min_guess:
        print("You Guess is too high \n") 
    else:
        print("Bad Input :) \n")

# Printing Conclusion Message
print("\n \t It's Over, Run the program again to start over \n \t")