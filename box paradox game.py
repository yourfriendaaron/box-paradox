'''
Bertand's Box Paradox: The Game
Version 0.21
further info: https://en.wikipedia.org/wiki/Bertrand%27s_box_paradox
'''

import random
import re

playagain = 'y'
numright = 0
numwrong = 0
g = re.compile('G$', re.IGNORECASE)
s = re.compile('S$', re.IGNORECASE)
yes = re.compile('YES$', re.IGNORECASE)
cheat = False
quitgame = False

def get_guess():
    guess = str(input('Type G to guess that the other coin will be gold. Type S to guess silver.\n'))
    if not (s.match(guess) or g.match(guess)):
        get_guess()
    guess = guess.upper()
    return guess

def samebox(boxtype, rightcoin):
    print('You reach into the box without looking, and draw a', boxtype, 'coin.')
    guess = get_guess()
    input('press Enter to look at the other coin in this box...')
    if guess == rightcoin:
        print('You were right!')
        global numright
        numright += 1
    else:
        print('You were wrong :(')
        global numwrong
        numwrong += 1

def diffbox():
    coindraw = random.choice(['gold', 'silver'])
    print('You reach into the box without looking, and draw a', coindraw, 'coin.')
    if coindraw == 'gold':
        rightcoin = 'S'
    if coindraw == 'silver':
        rightcoin = 'G'
    guess = get_guess()
    input('press Enter to look at the other coin in this box...')
    if guess == rightcoin:
        print('You were right!')
        global numright
        numright += 1
    else:
        print('You were wrong :(')
        global numwrong
        numwrong += 1

while True:
    startgame = str(input('''There are three boxes in front of you.'
'One has two silver coins, another has a silver and a gold coin, and the remaining box contains two gold coins.'
'Would you like to play a game? Type YES to continue...\n'''))
    if yes.match(startgame):
        break
    if startgame == 'UUDDLRLRBA':
        cheat = True
        break

while quitgame != 'Q':
    print('''     _______      _______      _______
    |       |    |       |    |       |
    | box 1 |    | box 2 |    | box 3 |
    |_______|    |_______|    |_______|''')
    while True:
        try:
            one23 = int(input('Select a box. Enter 1 2 or 3...\n'))
        except ValueError:
            pass
        else:
            if 1 <= one23 <= 3:
                break
    box = random.choice(['box SS', 'box SG', 'box GG'])
    if cheat == True:
        print(box)
    if box == 'box SS':
        samebox('silver', 'S')
    if box == 'box GG':
        samebox('gold', 'G')
    if box == 'box SG':
        diffbox()
    quitgame = input('Press Enter to play again or type Q to quit and see your results...\n').upper()

accuracy = (numright / (numright + numwrong)) * 100

print('Your overall accuracy was', accuracy, '%')
input('Thanks for playing! Press Enter to exit...')