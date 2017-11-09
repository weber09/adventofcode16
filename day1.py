

class Day1:
    def __init__(self):
        self.movements = {"N": [0,1], "S": [0,-1], "E": [1,0], "W": [-1,0]}
        self.visited = dict()
        self.crossed = False
        self.cross_point = 0, 0
        self.x = 0
        self.y = 0

    def solve(self, instr_input):
        instructions = instr_input.split(",")
        angle = 90
        right_dist = 0
        up_dist = 0
        distance = 0

        for j in range(len(instructions)):
            angle = self.get_angle(angle, instructions[j].strip())
            moved_dist = self.get_distance(instructions[j])
            direction = self.get_direction(angle)
            if angle == 180 and right_dist > 0:
                distance = (distance - right_dist) + abs(right_dist - moved_dist)
            elif angle == 0 and right_dist < 0:
                distance = (distance + right_dist) + abs(moved_dist + right_dist)
            elif angle == 90 and up_dist < 0:
                distance = (distance + up_dist) + abs(moved_dist + up_dist)
            elif angle == 270 and up_dist > 0:
                distance = (distance - up_dist) + abs(up_dist - moved_dist)
            else:
                distance += moved_dist
            right_dist, up_dist = self.get_dist_pos(angle, moved_dist, right_dist, up_dist)
            for i in range(moved_dist):
                self.walk(direction, moved_dist)

        return distance, abs(self.cross_point[0]) + abs(self.cross_point[1])

    def walk(self, direction, distance):
        if self.crossed:
            return

        self.x += self.movements[direction][0]
        self.y += self.movements[direction][1]

        pos = self.x, self.y

        if pos in self.visited.keys():
            self.crossed = True
            self.cross_point = pos
            self.visited[pos] += 1
        else:
            self.visited[pos] = 1


    def get_distance(self, instruction):
        return int(instruction.strip()[1:])

    def get_angle(self, angle, instruction):
        if instruction[0] == 'R':
            angle -= 90
        else:
            angle += 90

        if angle < 0:
            angle += 360

        if angle >= 360:
            angle -= 360

        return angle

    def get_dist_pos(self, angle, moved_dist, right_dist, up_dist):
        if angle == 0:
            right_dist += moved_dist
        elif angle == 180:
            right_dist -= moved_dist
        elif angle == 90:
            up_dist += moved_dist
        else:
            up_dist -= moved_dist
        return right_dist, up_dist

    def get_direction(self, angle):
        direction = "N"
        if angle == 0:
            direction = "E"
        elif angle == 270:
            direction = "S"
        elif angle == 180:
            direction = "W"
        return direction


