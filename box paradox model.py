'''
Bertand's Box Paradox: A Simulation
Version 0.2
further info: https://en.wikipedia.org/wiki/Bertrand%27s_box_paradox
'''

import random

goldright = 0
golddraw = 0
silverright = 0
silverdraw = 0
n = 0

print('''
This model will simulate Bertrand's Box Paradox in the following way:
It will randomly select one of the three boxes and draw a coin from the box.
Then it simulates a guess of the remaining coin in the box by guessing the same color of the coin it just drew.
The final accuracy displayed after the simulation is over proves the correct interpretation of the paradox.\n''')
numsims = int(input('How many times to run the simulation?\n'))

def goldbox():
    print('You have drawn a gold coin.\nSo your guess will be gold.')
    print('You were right!')
    global goldright
    goldright += 1
    global golddraw
    golddraw += 1

def silverbox():
    print('You have drawn a silver coin.\nSo your guess will be silver.')
    print('You were right!')
    global silverright
    silverright += 1
    global silverdraw
    silverdraw += 1

def diffbox():
    coindraw = random.choice(['gold', 'silver'])
    print('You have drawn a ', coindraw, ' coin.\nSo your guess will be ', coindraw, '.', sep='')
    if coindraw == 'gold': # You drew a gold coin, so you've guessed gold.
        global golddraw
        golddraw += 1
        print('You were wrong :(') # But it can't be the gold coin, since the only remaining coin in the box would be the silver coin.
    if coindraw == 'silver':
        global silverdraw
        silverdraw += 1
        print('You were wrong :(')

while n < numsims:
    box = random.choice(['box SS', 'box SG', 'box GG'])
    print(box)
    if box == 'box SS':
        silverbox()
    if box == 'box GG':
        goldbox()
    if box == 'box SG':
        diffbox()
    print()
    n += 1

print('When you drew a gold coin this was your chance of having drawn another gold coin:\n', ((goldright / golddraw) * 100), '%')
print('When you drew a silver coin this was your chance of having drawn another silver coin:\n', ((silverright / silverdraw) * 100), '%')
print('Your overall accuracy was', (((goldright + silverright) / n) * 100), '%')
input('Thanks for playing! Press Enter to exit...')