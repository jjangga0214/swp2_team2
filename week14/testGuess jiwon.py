import unittest

from guess import Guess


class TestGuess(unittest.TestCase):
    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('aback')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('u')  # 같은 문자가 한번 더 들어왔을 때 아무런 변화 x
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ _ ')
        self.g2.guess('a')  # 두번 나오는 알파벳도 한번에 보이게 출력
        self.assertEqual(self.g2.displayCurrent(), 'a _ a _ _ ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('u')  # 같은 문자가 한번 더 들어왔을 때 아무런 변화 x
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    def testGuess(self):
        self.assertEqual(self.g1.guessedChars, {'', 'n', 'e'})  # 이용된 글자들의 집합을 나타내는 데이터 처리
        self.assertEqual(self.g1.currentStatus, '_e_____')  # 부분적으로 맞추어진 단어의 상태

        self.g1.guess('a')  # 맞췄을 때
        self.assertEqual(self.g1.guessedChars, {'', 'e', 'a', 'n'})  # 이용된 글자들의 집합을 나타내는 데이터 처리
        self.assertEqual(self.g1.currentStatus, '_e_a___')  # 부분적으로 맞추어진 단어의 상태
        self.assertTrue(self.g1.guess('a'))  # 리턴값이 올바른지 (포함되니까 True 리턴)
        self.assertFalse(self.g1.finished())  # 정답을 아직 맞추지 못했을 때 데이터 처리

        self.g1.guess('k')  # 맞추지 못했을 때
        self.assertEqual(self.g1.guessedChars, {'', 'e', 'a', 'n', 'k'})
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertFalse(self.g1.guess('k'))  # 리턴값이 올바른지 (포함안되니까 False 리턴)
        self.assertFalse(self.g1.finished())

        self.g1.guess('d')
        self.assertEqual(self.g1.guessedChars, {'', 'd', 'e', 'a', 'n', 'k'})
        self.assertEqual(self.g1.currentStatus, 'de_a___')
        self.assertTrue(self.g1.guess('d'))
        self.assertFalse(self.g1.finished())

        self.g1.guess('f')
        self.assertEqual(self.g1.guessedChars, {'', 'd', 'e', 'f', 'a', 'n', 'k'})
        self.assertEqual(self.g1.currentStatus, 'defa___')
        self.assertTrue(self.g1.guess('f'))
        self.assertFalse(self.g1.finished())

        self.g1.guess('u')
        self.assertEqual(self.g1.guessedChars, {'', 'd', 'e', 'f', 'a', 'u', 'n', 'k'})
        self.assertEqual(self.g1.currentStatus, 'defau__')
        self.assertTrue(self.g1.guess('u'))
        self.assertFalse(self.g1.finished())

        self.g1.guess('l')
        self.assertEqual(self.g1.guessedChars, {'', 'd', 'e', 'f', 'a', 'u', 'l', 'n', 'k'})
        self.assertEqual(self.g1.currentStatus, 'defaul_')
        self.assertTrue(self.g1.guess('l'))
        self.assertFalse(self.g1.finished())

        self.g1.guess('t')
        self.assertEqual(self.g1.guessedChars, {'', 'd', 'e', 'f', 'a', 'u', 'l', 't', 'n', 'k'})
        self.assertEqual(self.g1.currentStatus, 'default')
        self.assertTrue(self.g1.guess('t'))
        self.assertTrue(self.g1.finished())


if __name__ == '__main__':
    unittest.main()
