input_ranges = []
input_info = []

after_ranges = False

with open('day_5/input.txt') as f:
    while True:
        input = f.readline().strip()

        if not input:
            if after_ranges:
                break

            after_ranges = True
            continue

        if not after_ranges:
            input_ranges.append([int(x) for x in input.split('-')])

        else:
            input_info.append(int(input))

count = 0 

# for each input, check each range, if in range increment count and break
for info in input_info:
    for bounds in input_ranges:
        if bounds[0] <= info <= bounds[1]:
            count += 1
            break

print(count)

# part 2

# first attempt: add values to hashset, then get length of hashset. does not work due to size of ranges.
# second attempt: merge overlapping ranges:
# conditions: end_1 >= start_2
# if overlapping, merge to [start_1, max(end_1, end_2)]
# repeat until no more overlaps
# no overlaps is when idx reaches len(input_ranges) - 1

input_ranges.sort()

idx = 0
while True:
    start_1, end_1 = input_ranges[idx]
    start_2, end_2 = input_ranges[idx+1]

    if end_1 >= start_2:
        new_range = [start_1, max(end_1, end_2)]
        input_ranges.pop(idx)
        input_ranges.pop(idx)
        input_ranges.insert(idx, new_range)
    else:
        idx += 1
    
    if idx >= len(input_ranges) - 1:
        break

count = 0

# end - start + 1 = number of integers in range
for bounds in input_ranges:
    count += bounds[1] - bounds[0] + 1

print(count)