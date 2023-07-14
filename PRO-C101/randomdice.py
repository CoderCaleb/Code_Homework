import random

def generateDice():
    isContinue = input('Press y to continue. Press n to exit: ')
    while isContinue == 'y':
        randNumber = random.randint(1, 6)
        if randNumber == 1:
            print('⚀')
        elif randNumber == 2:
            print('⚁')
        elif randNumber == 3:
            print('⚂')
        elif randNumber == 4:
            print('⚃')
        elif randNumber == 5:
            print('⚄')
        elif randNumber == 6:
            print('⚅')
        isContinue = input('Press y to continue. Press n to exit: ')

generateDice()
