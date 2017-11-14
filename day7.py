class Day7():
    def solve(self, msg):
        ip_count = 0
        ssl_count = 0
        lines = msg.split('\n')
        for i in range( len(lines)):
            line = lines[i]
            inside_bracket = False
            invalid = False
            has_it = False
            bab_list = []
            bab_list_inside = []
            has_ssl = False
            for j in range(len(line) - 2):
                if line[j] == '[':
                    inside_bracket = True
                    continue
                elif line[j] == ']':
                    inside_bracket = False
                    continue
                if not invalid and j < len(line) - 3 and \
                     line[j:j+2] == line[j+2:j+4][::-1] and \
                     line[j] != line[j+1]:
                    if inside_bracket:
                        invalid = True
                    else:
                        has_it = True
                if line[j] == line[j + 2]:
                    bab_str = line[j] + line[j + 1] + line[j]
                    if inside_bracket and bab_str in bab_list:
                        has_ssl = True
                    elif inside_bracket:
                        bab_list_inside.append(line[j+1] + line[j] + line[j+1])
                    elif bab_str in bab_list_inside:
                        has_ssl = True
                    else:
                        bab_list.append(line[j+1] + line[j] + line[j+1])
            if has_it and not invalid:
                ip_count += 1
            if has_ssl:
                ssl_count += 1
        return ip_count, ssl_count
