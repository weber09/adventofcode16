

class Day3:
    def solve(self, values):
        lin_val = values.split('\n')
        num_tri = 0
        for l in range(len(lin_val)):
            vals = lin_val[l].strip().split('  ')
            if len(vals) == 3 and \
               (int(vals[0]) + int(vals[1])) > int(vals[2]) and \
                    (int(vals[1]) + int(vals[2])) > int(vals[0]) and \
                    (int(vals[0]) + int(vals[2])) > int(vals[1]):
                num_tri += 1

        return num_tri
