import re
from enum import Enum
import random


class HangMan:
    picture = \
        '''\
        ____
        | |
        | 0
        |213
        | 4
        |5 6
        _|_
        | |______
        | |
        |__________|\
        '''
    replacements = ('O', '|', '/', '\\', '|', '/', '\\')
    max_life = len(replacements)

    def __init__(self):
        self._life = HangMan.max_life

    @property
    def life(self):
        return self._life

    def minuslife(self):
        self._life -= 1

    @property
    def status(self):
        current = HangMan.picture
        for i in range(HangMan.max_life):
            if i < HangMan.max_life - self._life:
                current = current.replace(str(i), HangMan.replacements[i])
            else:
                current = current.replace(str(i), ' ')

        return current

    def __str__(self):
        return self.status


class HangManService:
    def __init__(self, *, filepath='words.txt', mode='user'):
        self.hangman = HangMan()
        self._rand_words = []
        self._filepath = filepath
        self.mode = mode
        self.reset()
        self._word = self._rand_words.pop()

    class Result(Enum):
        ALREADY = 'ALREADY'
        SUCCESS = 'SUCCESS'
        CLEAR = 'CLEAR'
        FAILURE = 'FAILURE'
        DEATH = 'DEATH'

    def reset(self):
        self.hangman = HangMan()
        if not len(self._rand_words):
            self.load_random_word()
        self._word = self._rand_words.pop()
        self._trials = [' ']

    def guess(self, char) -> Result:
        if self.mode == 'developer':
            print(self._word)
        if char in self._trials:  # 이미 시도한 경우
            return HangManService.Result.ALREADY
        self._trials.append(char)
        if char in self._word:  # 맞은 경우
            if self.current_word == self._word:  # 단어를 완저히 맞춘 경우
                return HangManService.Result.CLEAR
            return HangManService.Result.SUCCESS
        else:  # 틀린  경우
            self.hangman.minuslife()
            if not self.hangman.life:  # 죽은 경우
                return HangManService.Result.DEATH
            return HangManService.Result.FAILURE

    def load_random_word(self, n=2):
        with open(self._filepath) as f:
            flen = sum(1 for line in list(f))
        with open(self._filepath) as f:

            rand_idxes = [random.randint(0, flen) for i in range(n)]
            rand_words = []
            for i, line in enumerate(f):
                if i in rand_idxes:
                    rand_words.append(line.strip())
        self._rand_words = rand_words

    @property
    def trials(self):
        return self._trials[1:]

    @property
    def current_word(self):

        rx = '[^%s]' % ''.join(self._trials)
        p = re.compile(rx)
        return p.sub('_', self._word)


class HangmanCliViewer:
    def __init__(self):
        self.service = HangManService()

    def _display(self):
        print(self.service.hangman)
        print('Current: %s' % self.service.current_word)
        print('Tries: %d' % len(self.service.trials))
        guessed_char = input('Select a letter: ')
        result = self.service.guess(guessed_char)
        if result is HangManService.Result.ALREADY:
            print('%s는 이미 시도한 문자입니다.' % guessed_char)
        elif result is HangManService.Result.SUCCESS:
            print('시도가 성공하였습니다.')
        elif result is HangManService.Result.CLEAR:
            self.service.reset()
            print('게임을 클리어하였습니다! 축하합니다!')
        elif result is HangManService.Result.FAILURE:
            print('시도가 실패하였습니다. 현재 목숨은 %d개입니다.' % self.service.hangman.life)
        else:  # 죽은 경우
            print(self.service.hangman)
            self.service.reset()
            print('Hangman 이 단두대에 매달려 게임이 종료됩니다.')
        return result

    def play(self):
        while True:
            result = None
            while result not in (HangManService.Result.CLEAR, HangManService.Result.DEATH):
                result = self._display()
            while True:
                decision = input('다음 게임을 이어서 진행하시겠습니까? (y/n)')
                if decision not in ('y', 'n'):
                    continue
                else:
                    break
            if decision is 'y':
                continue
            elif decision is 'n':
                print("게임을 플레이해주셔서 감사합니다.")
                break


if __name__ == '__main__':
    cli_viewer = HangmanCliViewer()
    cli_viewer.play()
