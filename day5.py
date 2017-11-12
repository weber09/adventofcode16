import hashlib


class Day5():
    def solve(self, door_id):
        solution = ""
        solution2 = [''] * 8
        j = 0
        m = 0
        for i in range(300000,39000000):
            h = hashlib.md5()
            h.update(door_id + str(i))
            if h.hexdigest()[:5] == '00000':
                if j < 8:
                    solution += h.hexdigest()[5:6]
                    j += 1
                index2 = int(h.hexdigest()[5:6], 16)
                val = h.hexdigest()[6:7]
                if m < 8 and index2 < 8 and solution2[index2] == '':
                    solution2[index2] = val
                    m += 1
            if j == 8 and m == 8:
                break
        return solution, ''.join(solution2)
