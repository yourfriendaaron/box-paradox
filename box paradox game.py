import random
import re

playagain = 'y'
numright = 0
numwrong = 0
g = re.compile('G', re.IGNORECASE)
s = re.compile('S', re.IGNORECASE)

def get_guess():
    guess = str(input('Type G to guess that the other coin will be gold. Type S to guess silver.\n'))
    if not (s.match(guess) or g.match(guess)):
        get_guess()
    guess = guess.upper()
    return guess

def samebox(boxtype, rightcoin):
    print('you have drawn a', boxtype, 'coin.')
    guess = get_guess()
    input('press Enter to look at the other coin in this box...')
    if guess == rightcoin:
        print('you were right!')
        global numright
        numright += 1
    else:
        print('you were wrong :(')
        global numwrong
        numwrong += 1

def diffbox():
    coindraw = random.choice(['gold', 'silver'])
    print('you have drawn a', coindraw, 'coin.')
    if coindraw == 'gold':
        rightcoin = 'S'
    if coindraw == 'silver':
        rightcoin = 'G'
    guess = get_guess()
    input('press Enter to look at the other coin in this box...')
    if guess == rightcoin:
        print('you were right!')
        global numright
        numright += 1
    else:
        print('you were wrong :(')
        global numwrong
        numwrong += 1

while playagain == 'y':
    box = random.choice(['box SS', 'box SG', 'box GG'])
    print(box)
    if box == 'box SS':
        samebox('silver', 'S')
    if box == 'box GG':
        samebox('gold', 'G')
    if box == 'box SG':
        diffbox()
    playagain = input('Play again? y or n\n')

accuracy = (numright / (numright + numwrong)) * 100

print('Your overall accuracy was', accuracy, '%')
input('Thanks for playing! Press Enter to exit...')