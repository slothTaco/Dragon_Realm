import random
import time

def displayIntro():
    print('''You are in a land full of dragons. Infront of you,
you see two caves. In one cave, the dragon is friendly and will
share his treasure with you. The other dragon is greedy and hungry,
and will eat you on sight.''')
    print()

def chooseCave():
    '''Asks player which cave they would like to go in, 1 or 2'''
    cave = ''
    while cave != '1' and cave !='2':
        print('Which cave will you go into?(1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    '''Explains what happens in the players chosen cave.
Randomizes ending depending which cave (1 or 2) player chose,
either eaten or get the treaure.
Asks if player would like to play again.'''
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! ' +
                'he opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave= random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

    print('Do you want to play again? (yes or no)')
    playAgain = input()

# Will terminate game if anything but 'y' or 'yes' is entered.
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

