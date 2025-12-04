# start at depth = 12.
# go from 0 to len-depth-1, find max digit and its index.
# append digit to result, call function again with str from index+1 and depth-1.
# at 0, return empty string.

def find_next_num(str, depth):

    # base case
    if depth == 0 or len(str) == 0:
        return ""

    # find first max digit and its index
    first_max = 0
    first_max_idx = 0

    # calculate the limit for the loop
    limit = len(str) - depth + 1

    for i in range(limit):
        if int(str[i]) > first_max:
            first_max = int(str[i])
            first_max_idx = i

        if first_max == 9:
            break

    return str[first_max_idx] + find_next_num(str[first_max_idx+1:], depth-1)



joltages = []

# part 1

# simple approach, find the left-most occurance of the maximum digit in the substring [start, end-2],
# then find the maximum digit in the substring [first_max_idx+1, end-1].

with open('day_3/input.txt') as f:
    
    while True:
        input = f.readline().strip()

        if not input:
            break

        first_max = 0
        first_max_idx = 0

        input_len = len(input)

        for i in range(input_len-1):
            if int(input[i]) > first_max:
                first_max = int(input[i])
                first_max_idx = i

            if first_max == 9:
                break

        second_max = 0

        for i in range(first_max_idx+1, input_len):
            if int(input[i]) > second_max:
                second_max = int(input[i])
            if second_max == 9:
                break
        
        joltages.append(first_max*10 + second_max)

print(sum(joltages))
        
# part 2

joltages = []


# recursive approach, since we need to do the above algorithm 12 times instead of twice.
# find the left-most occurance of the maximum digit in the substring [start, end-depth],
# then call the function again with the substring [first_max_idx+1, end-(depth-1)] and depth-1, repeat until depth = 0.
with open('day_3/input.txt') as f:
    
    while True:
        input = f.readline().strip()

        if not input:
            break

        result = find_next_num(input, 12)
        joltages.append(int(result))

print(sum(joltages))