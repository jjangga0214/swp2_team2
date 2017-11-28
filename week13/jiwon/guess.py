class Guess:
    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = "_" * len(self.secretWord)

    def display(self):
        print("Current: ", self.currentStatus)
        print("Tries:", self.numTries)
        print("GuessedChars:", self.guessedChars)


    def guess(self, character):
        count = 0
        self.guessedChars.append(character)

        for i in range(len(self.secretWord)):
            if self.secretWord[i] == character:
                self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]

            elif self.secretWord[i] != character:
                count += 1

        if count == len(self.secretWord):
            self.numTries += 1

        if self.currentStatus.isalpha():
            return True


    






