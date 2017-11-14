import unittest
import day7


class Test_Day7(unittest.TestCase):
    def test_inpout1(self):
        test_case = "abba[mnop]qrst\n" \
                    "abcd[bddb]xyyx\n" \
                    "aaaa[qwer]tyui\n" \
                    "ioxxoj[asdfgh]zxcvbn"
        ans = day7.Day7().solve(test_case)
        self.assertEqual(ans[0], 2)

    def test_input2(self):
        test_case = "aba[bab]xyz\n" \
                    "xyx[xyx]xyx\n" \
                    "aaa[kek]eke\n" \
                    "zazbz[bzb]cdb\n" \
                    "kek[aaa]eke"
        ans = day7.Day7().solve(test_case)
        self.assertEqual(ans[1], 3)

    def test_default(self):
        f = open("day7_input", "r")
        test_case = f.read()
        ans = day7.Day7().solve(test_case)
        print(ans[1])
        self.assertEqual(ans[0], 118)
