import random

word = ['mafia', 'krodil', 'python', ]


def generate_word(word_List):
    wordChose = random.randint(0, len(word) - 1)

    return word_List[wordChose]


def displayBoard(missedLetters, correctLetters, secretWord):
    print('oshibo4nie bukvy:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guess):
    while True:
        print('vvedite vukvy')
        gues = input()
        gues = gues.lower()

        if len(gues) != 1:
            print('vvedite 1 bukvy ')
        elif gues in already_guess:
            print('vi uje nazivali etu bykvy')
        elif gues not in 'abcdefghijklmnopqrstuvwxyz':
            print('vvedite korrektno bukvy')
        else:
            return gues


def play_again():
    print('ewe raz??')
    return input().lower().startswith('d')


print('V I S E L I C A')
missedLetters = ''
correctLetters = ''
secretWord = generate_word(word)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = get_guess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        Found_letters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                Found_letters = False
                break
        if Found_letters:
            print('Pobedka! eto slovo - ' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == 5:

            print('ti proigral, eto slovo - ' + secretWord)
            gameIsDone = True
    if gameIsDone:
        break




