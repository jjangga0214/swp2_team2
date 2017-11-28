class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = ['_' for i in range(len(word))]

    def display(self):
        current = ''
        for i in self.currentStatus:
            current += i
        print('Current: %s' % current)
        print('Tries: %d' % self.numTries)

    def guess(self, character):
        self.guessedChars.append(character)
        if character in self.secretWord:
            for i in range(len(self.currentStatus)):
                if self.secretWord[i] == character:
                    self.currentStatus[i] = character
        else:
            self.numTries += 1

        if '_' in self.currentStatus:
            return False
        else:
            return True



