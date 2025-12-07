import numpy as np


lines = []
with open('day_7/input.txt') as f:
    while True:
        line = list(f.readline().strip())
        if not line:
            break
        lines.append(line)

def parse_line(lines, line_idx):
    temp = 0
    for i in range(len(lines[line_idx])):
        # set beam below start
        if lines[line_idx-1][i] == 'S':
            lines[line_idx][i] = '|'
        
        # if beam above, continue beam if empty space in current line, split if splitter
        elif lines[line_idx-1][i] == '|':
            if lines[line_idx][i] == '.':
                lines[line_idx][i] = '|'

            elif lines[line_idx][i] == '^':
                temp+=1
                if i-1 >= 0:
                    lines[line_idx][i-1] = '|'
                if i+1 < len(lines[line_idx]):
                    lines[line_idx][i+1] = '|'

    return temp


def track_beams(lines, line_idx, col_idx, count_cache):
    # cases to check:
    # 1. at top of the tree. Return 1. Termination case, can't be zero because the case with 0 splitters has 1 path.

    # 2. current position is a beam. Check left and right for beams. If found, continue up that way.
    
    # print(line_idx, col_idx)

    # base case. Count = 1. Each 'path' that reaches the top counts as 1.
    if lines[line_idx][col_idx] == 'S':
        return 1
    
    if line_idx-1 < 0:
        return 0

    count = 0

    # if we are looking at a beam.
    if lines[line_idx][col_idx] == '|':
        
        # check left and right for beams
        if col_idx-1 >= 0 and lines[line_idx][col_idx-1] == '^':
            if count_cache[line_idx-1][col_idx-1] != -1:
                count += count_cache[line_idx-1][col_idx-1]
            else:
                count_cache[line_idx-1][col_idx-1] = track_beams(lines, line_idx-1, col_idx-1, count_cache)
                count += count_cache[line_idx-1][col_idx-1]
        
        if col_idx+1 < len(lines[line_idx]) and lines[line_idx][col_idx+1] == '^':
            if count_cache[line_idx-1][col_idx+1] != -1:
                count += count_cache[line_idx-1][col_idx+1]
            else:
                count_cache[line_idx-1][col_idx+1] = track_beams(lines, line_idx-1, col_idx+1, count_cache)
                count += count_cache[line_idx-1][col_idx+1]

        if count_cache[line_idx-1][col_idx] != -1:
            count += count_cache[line_idx-1][col_idx]
        else:
            count_cache[line_idx-1][col_idx] = track_beams(lines, line_idx-1, col_idx, count_cache)
            count += count_cache[line_idx-1][col_idx]
        

    return count
        
count = 0

for line_idx in range(1, len(lines)):
    count += parse_line(lines, line_idx)

# print(lines)
out_str = ''
for line in lines:
    out_str += ''.join(line) + '\n'

with open('day_7/output.txt', 'w') as f:
    f.write(out_str)

print(count)

# part 2: parse it after constructing the tree? 
# naive idea:
# for each beam in the last line, trace it up to a split, then check up left and up right for other beams
# increment count for each split, then call recursive function on each split.

count_cache = np.array([[-1 for _ in range(len(lines[0]))] for _ in range(len(lines))])

count = 0
for i in range(len(lines[-1])):

    count += track_beams(lines, len(lines)-1, i, count_cache)

print(count)