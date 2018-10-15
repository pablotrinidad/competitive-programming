import unittest
from solution import question_marks

class TestQuestionMarks(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, question_marks('arrb6???4xxbl5???eee5'))

    def test_02(self):
        self.assertEqual(False, question_marks('aa6?9'))

    def test_03(self):
        self.assertEqual(True, question_marks('acc?7??sss?3rr1??????5ff'))

    def test_04(self):
        self.assertEqual(False, question_marks('5???5xdc2????8fsy1???cvd9cdx'))


if __name__ == '__main__':
    unittest.main()
