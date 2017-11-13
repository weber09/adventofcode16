class Day6():
    def solve(self, msg):
        msg_lines = msg.split("\n")
        message = ''
        message2 = ''
        for i in range(len(msg_lines[0])):
            counts = [0] * 26
            for j in range(len(msg_lines)):
                if msg_lines[j] == '':
                    continue
                l = ord(msg_lines[j][i]) - 97
                counts[l] += 1
            mostLetter = 0
            least_letter = 0
            higherFreq = -1
            least_freq = 10000000
            for j in range(26):
                if counts[j] > higherFreq:
                    mostLetter = j
                    higherFreq = counts[j]
                if counts[j] > 0 and counts[j] < least_freq:
                    least_letter = j
                    least_freq = counts[j]
            message += str(unichr(mostLetter + 97))
            message2 += str(unichr(least_letter + 97))

        return message, message2
