class Day2:
    def __init__(self):
        self.moves = {"U": [0, -1], "D": [0, 1], "R": [1, 0], "L": [-1, 0]}
        self.pos = [0, 2]
        self.m = [["", "", "1", "", ""],
                  ["", "2", "3", "4", ""],
                  ["5", "6", "7", "8", "9"],
                  ["", "A", "B", "C", ""],
                  ["", "", "D", "", ""]]

    def solve(self, instructions):
        m_inst = instructions.split('\n')
        code = ""
        for i in range(len(m_inst)):
            for j in range(len(m_inst[i])):
                move = m_inst[i][j]
                if move == "U" and self.pos[1] > 0 and self.m[self.pos[1] + self.moves[move][1]][self.pos[0]] != "":
                    self.pos[1] += self.moves[move][1]
                elif move == "D" and self.pos[1] < 4 and self.m[ self.pos[1] + self.moves[move][1]][self.pos[0]] != "":
                    self.pos[1] += self.moves[move][1]
                elif move == "R" and self.pos[0] < 4 and self.m[self.pos[1]][self.pos[0] + self.moves[move][0]] != "":
                    self.pos[0] += self.moves[move][0]
                elif move == "L" and self.pos[0] > 0 and self.m[ self.pos[1]][self.pos[0] + self.moves[move][0]] != "":
                    self.pos[0] += self.moves[move][0]
            code += self.m[self.pos[1]][self.pos[0]]
        return code
