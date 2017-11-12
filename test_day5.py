import unittest
import day5


class Test_day5(unittest.TestCase):
    def test_case1(self):
        test_case = "abc"
        ans = day5.Day5().solve(test_case)
        self.assertEqual(ans[0], "18f47a30")

    def test_case2(self):
        test_case = "abc"
        ans = day5.Day5().solve(test_case)
        self.assertEqual(ans[1], "05ace8e3")

    def test_defaultCase(self):
        test_case = "ugkcyxxp"
        ans = day5.Day5().solve(test_case)
        print(ans[1])
        self.assertEqual(ans[0], "d4cd2ee1")
