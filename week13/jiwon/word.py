import random


class Word:

    def __init__(self, filename):

        # 파일을 열어서 행별로 구분한 리스트를 만들고 파일을 닫음
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        # 각 행의 오른쪽 공백문자를 제거하고 self.words 리스트에 덧붙임 (이 수효를 self.count 에 기록
        self.count = 0
        for line in lines:
            word = line.rstrip()  # 오른쪽 공백문자 제거 그 단어 하나를 읽음 한줄에 한단어씩 있으니까
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)  # 몇개의 단어가 있는지

    def test(self):
        return 'default'

    def randFromDB(self):

        r = random.randrange(self.count)  # randrange 에 어떤 인자를 주면 호출할때마다 0부터 9까지의 범위내의 난수가 발생함
        return self.words[r]
