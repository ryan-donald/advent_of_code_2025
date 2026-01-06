import time
# each @ represents a roll, if the roll has less than 4 in the 8 adjacent cells (horizontally, vertically, diagonally)
# it is valid and can be picked. Mark as X when picked.
def valid_roll(lines, x, y):

    count = 0

    # need to check all adjacent cells
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i < 0 or i >= len(lines[0]):
                continue
            if j < 0 or j >= len(lines):
                continue
            if i == y and j == x:
                continue
            if lines[i][j] == '@':
                count += 1

    if count < 4:
        lines[y][x] = 'X'
        return True
    return False

# call after removing a roll to see if any nearby rolls can now be picked
def check_nearby_rolls(lines, x, y):
    count = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i < 0 or i >= len(lines[0]):
                continue
            if j < 0 or j >= len(lines):
                continue
            if lines[i][j] == '@':
                if valid_roll(lines, j, i):
                    count += check_nearby_rolls(lines, j, i)
                    count += 1
    return count


with open('day_4/input.txt') as f:
    # lines = f.readlines()
    lines = [list(line.strip()) for line in f.readlines()]

# start = time.perf_counter()
# # simulate until no more valid rolls can be picked. not the best approach, but brute force. 
# num_valid = 0
# while True:
#     prev_num_valid = num_valid

#     for y in range(len(lines)):
#         for x in range(len(lines[0])):
#             if lines[y][x] == '@':
#                 if valid_roll(lines, x, y):
#                     num_valid +=1

#     if prev_num_valid == num_valid:
#         break

# end = time.perf_counter()

# print(f"Time taken: {end - start} seconds")

# print(f'part 1: {num_valid}')


# optimized approach, starts the same as above, except whenever a roll is picked recursively
# check nearby rolls to see if they are now valid. Now we only recheck rolls that could be affected by the removal.
# start = time.perf_counter()
num_valid = 0

for y in range(len(lines[0])):
    for x in range(len(lines)):
        if lines[y][x] == '@':
            if valid_roll(lines, x, y):
                num_valid +=1

                num_valid += check_nearby_rolls(lines, x, y)
                        
# end = time.perf_counter()

# print(f"Time taken: {end - start} seconds")
print(f'part 2: {num_valid}')
