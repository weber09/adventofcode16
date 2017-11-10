import unittest
import day4


class TestDay4(unittest.TestCase):
    def test_inputTest1(self):
        test_case = "aaaaa-bbb-z-y-x-123[abxyz]\n" \
                    "a-b-c-d-e-f-g-h-987[abcde]\n" \
                    "not-a-real-room-404[oarel]\n" \
                    "totally-real-room-200[decoy]"
        ans = day4.Day4().solve(test_case)
        self.assertEqual(ans[0], 1514)

    def test_inputTest2(self):
        test_case = "qzmt-zixmtkozy-ivhz-343[zimth]"
        ans = day4.Day4().solve(test_case)
        self.assertEqual(ans[1][0], 'very encrypted name')

    def test_defaultInput(self):
        f = open('day4_input', 'r')
        test_case = f.read()
        ans = day4.Day4().solve(test_case)
        f = open('day4_output', 'w')
        f.write(ans[1])
        self.assertEqual(ans[0], 173787)