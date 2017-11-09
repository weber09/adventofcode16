import unittest
import day1


class TestDay1(unittest.TestCase):
    def test_testCase1(self):
        testCase = "R2, L3"
        answ, _ = day1.Day1().solve(testCase)
        self.assertEqual(answ, 5)

    def test_testCase2(self):
        testCase = "R2, R2, R2"
        answ, _ = day1.Day1().solve(testCase)
        self.assertEqual(answ, 2)

    def test_testCase3(self):
        testCase = "R5, L5, R5, R3"
        answ, _ = day1.Day1().solve(testCase)
        self.assertEqual(answ, 12)

    def test_defaultInput(self):
        testCase = "R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, " \
                   "L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, " \
                   "L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, " \
                   "R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, " \
                   "L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, " \
                   "R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, " \
                   "R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, " \
                   "R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, " \
                   "L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1"

        answ = day1.Day1().solve(testCase)

        print(answ[1])

        self.assertEqual(answ[0], 271)


    def test_defaultInput2(self):
        testCase = "R8, R4, R4, R8"

        answ, asw2 = day1.Day1().solve(testCase)

        self.assertEqual(answ, 8)
        self.assertEqual(asw2, 4)

    def test_myInput(self):
        testCase = "R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2"

        answ, _ = day1.Day1().solve(testCase)
        #7
        #13
        self.assertEqual(answ, 20)
