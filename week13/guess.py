class Guess:

    def __init__(self, word):
        self.Wordlist = list(self.word)
        self.guessedChars = []
        self.numTries = 0
        self.nowlist = []
        for i in range(len(self.word)):
            self.nowlist.append("_")


    def display(self):
        print("Current: " + self.Wordlist)
        print("Tries: " + self.numTries)

    def guess(self, character):
        if self.character in self.Wordlist:
            for i in range(len(self.Wordlist)):
                if self.character == self.Wordlist[i]:
                    self.nowlist[i].replace(self.chracter)
            if self.nowlist == self.Wordlist:
                for i in range(len(self.nowlist)):
                    print(self.nowlist[i], end='')
                return True
            else:
                return False
        else:
            self.numTries += 1