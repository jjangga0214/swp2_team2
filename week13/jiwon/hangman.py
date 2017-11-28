class Hangman:
    text = [

        # 블록문자열
        # \\ == 오른쪽 팔, 오른쪽 다리
        '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''',

        '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\
''',

        '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

        '''\
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

        '''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

        '''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

        '''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

    ]

    def getLife(self):
        return len(self.text) - 1  # 목숨의 갯수

    def get(self, life):
        return self.text[life]  # 목숨에 해당하는 그림들 life == 6이면
        # 목숨 6개 남아있는 그림 이런식으로