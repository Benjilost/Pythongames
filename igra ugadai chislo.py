# Ugaday 4islo
import random


def choseNum():
    num = ''
    while num != int:
        print('vvedite chislo')
        num = input()


GuessTaken = 0

print('Privet. Kak tebya zovut?!')
MyName = input()
for name in range(6):
    if MyName == 'xyecoc':
        print('vvedi drugoe imya')
        MyName = input()
    else:
        break

number = random.randint(1, 100)
print('4to j ' + MyName + ' ya zagadivay 4islo ot 1 do 100')

for GuessTaken in range(5):
    print('Poprobyu ugadat')
    gues = input()
    gues = int(gues)

    if gues < number:
        print('tvoe 4islo slishkom malenkoe')

    if gues > number:
        print('tvoe 4islo slishkom bolshoe')

    if gues == number:
        break

if gues == number:
    GuessTaken = str(GuessTaken + 1)
    print('otli4no ya zagadala ' + str(number) + MyName + ' ti spravilsa za ' + GuessTaken + ' popitok'
          )

if gues != number:
    number = str(number)
    print('ti proigral, ya zagadala 4islo ' + number)
