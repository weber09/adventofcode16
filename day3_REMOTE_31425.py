

class Day3:
    def solve(self, values):
        lin_val = values.split('\n')
        num_tri = 0
        num_tri_col = 0
        n = len(lin_val)
        for l in range(n):
            vals = list(filter(None, lin_val[l].strip().split(' ')))
            if l % 3 == 0 and l < n - 3:
                vals1 = list(filter(None, lin_val[l+1].strip().split(' ')))
                vals2 = list(filter(None, lin_val[l+2].strip().split(' ')))
                if len(vals) == 3 and len(vals1) == 3 and len(vals2) == 3:
                    if self.is_triangle(vals[0], vals1[0], vals2[0]):
                        num_tri_col += 1
                    if self.is_triangle(vals[1], vals1[1], vals2[1]):
                        num_tri_col += 1
                    if self.is_triangle(vals[2], vals1[2], vals2[2]):
                        num_tri_col += 1

            if len(vals) == 3 and\
               self.is_triangle(vals[0], vals[1], vals[2]):
                num_tri += 1

        return num_tri, num_tri_col

    def is_triangle(self, val1, val2, val3):
        return int(val1) + int(val2) > int(val3) and \
               int(val2) + int(val3) > int(val1) and \
               int(val1) + int(val3) > int(val2)
