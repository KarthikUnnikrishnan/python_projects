import random
from collections import Counter

# creating list with fruits words
wordslist = '''apple banana mango orange lemon'''
wordslist = wordslist.split(' ')

# selecting random words from list
word = random.choice(wordslist)

if __name__ == '__main__':
    
    print('\nGuess the word!\n')
    print("Words Are: Apple, Banana, Mango, Orange, Lemon \n")

for i in word:
    print('_', end=' ')
print(__name__)

playing = True

# list for storing the letters guessed by the player

letterGuessed = ''
chances = len(word) + 2
correct = 0
flag = 0
try:
    while (chances!=0) and flag == 0:
        print()
        chance -= 1
        
        try:
            guess = str(input("Enter a letter to guess: "))
        except:
            print("Enter only a letter!")
            continue
        
        
        
