import unittest
import day3


class TestDay3(unittest.TestCase):
    def test_defaultTest(self):
        test_case = "5  10  25"
        ans = day3.Day3().solve(test_case)
        self.assertEqual(ans, 0)

    def test_testCase1(self):
        test_case = "25  10  5"
        ans = day3.Day3().solve(test_case)
        self.assertEqual(ans, 0)

    def test_testCase2(self):
        test_case = "10  25  5"
        ans = day3.Day3().solve(test_case)
        self.assertEqual(ans, 0)

    def test_testCase3(self):
        test_case = "541  588  421"
        ans = day3.Day3().solve(test_case)
        self.assertEqual(ans, 1)

    def test_deafultInput(self):
        f = open("day3_input", "r")
        test_case = f.read()
        ans = day3.Day3().solve(test_case)
        self.assertEqual(ans, 0)
