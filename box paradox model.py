import random
import re

playagain = 'y'
numright = 0
numwrong = 0
g = re.compile('G', re.IGNORECASE)
s = re.compile('S', re.IGNORECASE)
n = 0

def samebox(boxtype, rightcoin):
    print('you have drawn a', boxtype, 'coin.')
    if boxtype == 'silver':
        guess = 'S'
    if boxtype == 'gold':
        guess = 'G'
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
        guess = 'G'
    if coindraw == 'silver':
        rightcoin = 'G'
        guess = 'S'
    if guess == rightcoin:
        print('you were right!')
        global numright
        numright += 1
    else:
        print('you were wrong :(')
        global numwrong
        numwrong += 1

while n <= 10000:
    box = random.choice(['box SS', 'box SG', 'box GG'])
    print(box)
    if box == 'box SS':
        samebox('silver', 'S')
    if box == 'box GG':
        samebox('gold', 'G')
    if box == 'box SG':
        diffbox()
    n += 1

accuracy = (numright / (numright + numwrong)) * 100

print('Your overall accuracy was', accuracy, '%')
input('Thanks for playing! Press Enter to exit...')
