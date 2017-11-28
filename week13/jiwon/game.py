from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())  # 랜덤하게 단어선택

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()  # 목숨의 개수를 초기화 시킴

    while guess.numTries < maxTries:  # 목숨이 몇개 남았는지 체크해줌

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:  # 한글자가 아니면
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:  # 이미 사용한 문자라면
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
        print('word : ' + guess.secretWord)
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
