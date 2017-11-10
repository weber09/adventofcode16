import collections

from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


class Day4:
    def solve(self, data):
        sum_ids = 0
        lines = data.split('\n')
        rooms_names = []
        for l in range(len(lines)):
            line = lines[l]
            if line == '':
                continue
            code_id = line.split('[')[0]
            checksum = line.split('[')[1][:-1]
            codeLst = code_id.split('-')

            code = sorted(OrderedCounter(''.join(sorted(''.join(codeLst[:-1])))).items(), key=lambda item: (-item[1], item[0]))
            id = int(codeLst[len(codeLst)-1])
            i = 0
            checks = True
            for k in range(len(checksum)):
                if checksum[k] != code[i][0]:
                    checks = False
                    break
                i += 1
            if checks:
                sum_ids += id
                rooms_names.append(self.decipher_room_name('-'.join(codeLst[:-1]), id))

        return sum_ids, '\n'.join(rooms_names)

    def decipher_room_name(self, cipher_name, id):
        room_name = ""
        for l in range(len(cipher_name)):
            if cipher_name[l] == '-':
                room_name += ' '
            else:
                room_name += str(unichr((((ord(cipher_name[l]) - 97) + id) % 26) + 97))
        return room_name + ' ' + str(id)
