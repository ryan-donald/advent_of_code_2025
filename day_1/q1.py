# initialize variables
count = 0
prev_val = 50

# read input line by line
with open('day_1/input.txt', 'r') as f:
    
    while(True):
        # read a line and store in input "{direction}{steps}"
        input = f.readline().strip('\n').split(' ')[0]

        # after reaching eof break the loop
        if not input:
            break

        # processes the input, checking left or right, then processing number of times '0' is at the top of the dial
        if input[0] == 'L':

            # handles full rotations
            curr_val = (prev_val - int(input[1:])) % 100
            count += int(input[1:]) // 100

            # handles rotations that cross '0' but are not full rotations
            if curr_val > prev_val and prev_val != 0:
                count += 1
            
            # handles case where we do not rotate accross '0' but stop at '0'
            elif curr_val == 0:
                count += 1

        # same as above but for right rotations
        elif input[0] == 'R':
            curr_val = (prev_val + int(input[1:])) % 100
            count += int(input[1:]) // 100

            if curr_val < prev_val and prev_val != 0:
                count += 1
            elif curr_val == 0:
                count += 1

        prev_val = curr_val

print(count)