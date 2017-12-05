import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('success')

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
        self.g1.guess('i')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ') # defalt에 없는 문자가 들어왔을 때
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ') # 예전에 입력했던 알파벳이 다시 들어왔을 때

        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ e _ _ ')
        self.g2.guess('s')
        self.assertEqual(self.g2.displayCurrent(), 's _ _ _ e s s ') # 같은 알파벳이 많이 있을 때, 모두 들어갔는지 확인

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('i')
        self.assertEqual(self.g1.displayGuessed(), ' a e i n t u ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e i n t u ')

        self.assertEqual(self.g2.displayGuessed(), ' e n ')
        self.g2.guess('s')
        self.assertEqual(self.g2.displayGuessed(), ' e n s ')

    def testGuess(self):
        self.assertTrue(self.g1.guess('a'))
        self.assertFalse(self.g1.guess('i'))


if __name__ == '__main__':
    unittest.main()
