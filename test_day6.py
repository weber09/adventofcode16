import unittest
import day6

class TestDay6(unittest.TestCase):
    def test_case1(self):
        test_case = "eedadn\n"\
                    "drvtee\n"\
                    "eandsr\n"\
                    "raavrd\n"\
                    "atevrs\n"\
                    "tsrnev\n"\
                    "sdttsa\n"\
                    "rasrtv\n"\
                    "nssdts\n"\
                    "ntnada\n"\
                    "svetve\n"\
                    "tesnvt\n"\
                    "vntsnd\n"\
                    "vrdear\n"\
                    "dvrsen\n"\
                    "enarar"
        ans = day6.Day6().solve(test_case)
        self.assertEqual(ans[0], "easter")

    def test_case2(self):
        test_case = "eedadn\n" \
                    "drvtee\n" \
                    "eandsr\n" \
                    "raavrd\n" \
                    "atevrs\n" \
                    "tsrnev\n" \
                    "sdttsa\n" \
                    "rasrtv\n" \
                    "nssdts\n" \
                    "ntnada\n" \
                    "svetve\n" \
                    "tesnvt\n" \
                    "vntsnd\n" \
                    "vrdear\n" \
                    "dvrsen\n" \
                    "enarar"
        ans = day6.Day6().solve(test_case)
        self.assertEqual(ans[1], "advent")

    def test_defaultInput(self):
        f = open("day6_input", "r")
        test_case = f.read()
        ans = day6.Day6().solve(test_case)
        print(ans[1])
        self.assertEqual(ans[0], "mshjnduc")
