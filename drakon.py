import random
import time


def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
Перед собой вы видите три пещеры.
В одной из них — дружелюбный дракон, который готов поделиться с вами своими сокровищами.
Во второй — жадный и голодный дракон, который мигом вас съест.''')
    print()


def choseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('В какую пещеру вы войдете? (нажмите клавишу 1, 2 или 3)')
        cave = input()

    return cave


def CheckCave(Chosen):
    print('вы приближаетесь к пещере....')
    time.sleep(2)
    print('ее темнота заставляет вас дрожать от страха....')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! он раскрывает свою пасть и....')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)
    drakon = random.randint(1, 3)
    while friendlyCave == drakon:
        drakon = random.randint(1, 3)

    if Chosen == str(friendlyCave):
        print('Делится с вами сокровищами!)))')
    elif Chosen == str(drakon):
        print('COCO')
    else:
        print('Моментально вас съедает')


playAgain = 'да'
while playAgain == 'да':
    displayIntro()
    caveNumber = choseCave()
    CheckCave(caveNumber)
    print('Попытаете удачу еще раз (да или нет)??')
    playAgain = input()
