import numpy as np
from z3 import *

def parse_line(parts):
    # parses the indicators into 0s and 1s for on/off
    indicators = parts[0]
    indicators = indicators.strip('[]')
    display = ""
    for i in range(len(indicators)):
        if indicators[i] == '.':
            display+='0'
        else:
            display+='1'
    # reverse so that position 0 is bit 0 (rightmost)
    indicators = display[::-1]

    # parses the joltages into a list
    joltage = parts[-1]
    joltage = joltage.strip('{}')
    joltage = joltage.split(',')
    joltages = []
    for jolt in joltage:
        joltages.append(int(jolt))
    joltage = joltages

    # parses the wiring connections into a list of lists
    wiring = parts[1:-1]
    for i in range(len(wiring)):
        part = wiring[i]
        part = part.strip('()')

        nums = []
        for num in part.split(','):
            nums.append(int(num))

        wiring[i] = nums

    return indicators, joltage, wiring

def find_min_presses(start_state, button_masks, target):
    # try all combinations of button presses to find minimum
    from itertools import combinations
    
    n = len(button_masks)
    
    # try pressing 0 buttons, then 1, then 2, etc.
    for num_presses in range(n + 1):
        for combo in combinations(range(n), num_presses):
            # apply XOR for all buttons in this combination
            state = start_state
            for button_idx in combo:
                state ^= button_masks[button_idx]
            
            if state == target:
                return num_presses
    
    return float('inf')  # unreachable

machines = []

with open('day_10/input.txt') as f:

    while True:
        line = f.readline().strip()

        if not line:
            break

        parts = line.split()

        machines.append(parts)

# parse display configuration as binary numbers

min_presses = []

for i in range(len(machines)):
    parts = machines[i]
    indicators, joltage, wiring = parse_line(parts)
    indicators = int(indicators, 2)

    # then for each button (index) in wiring, for each connection create XOR mask
    button_masks = []
    for button in wiring:
        mask = 0
        for connection in button:
            # set the bit at position 'connection'
            mask |= (1 << connection)
        
        button_masks.append(mask)

    start_state = 0
    target_state = indicators
    
    # for part 2: solve system of linear equations
    # build coefficient matrix A where A[i][j] = 1 if button j affects joltage i
    num_joltages = len(joltage)
    num_buttons = len(wiring)
    
    # create coefficient matrix
    A = np.zeros((num_joltages, num_buttons), dtype=int)
    for button_idx, connections in enumerate(wiring):
        for joltage_idx in connections:
            A[joltage_idx][button_idx] = 1
    
    b = np.array(joltage)
    
    # use z3 optimizer to minimize the number of button presses
    opt = Optimize()
    
    # create variables to be tuned. these represent each button press count
    x_vars = [Int(f'x_{j}') for j in range(num_buttons)]

    # add constraints: A * x = b and x >= 0. this essentailly means the sum of button presses that effect a given joltage must equal the target.
    opt.add([Sum([A[i][j] * x_vars[j] for j in range(num_buttons)]) == b[i] for i in range(num_joltages)])
    # this ensures that button presses are non-negative.
    opt.add([x_vars[j] >= 0 for j in range(num_buttons)])
    
    # minimize the sum of button presses
    opt.minimize(Sum(x_vars))

    # if a solution is possible
    if opt.check() == sat:
        m = opt.model()
        total_presses = sum([m[x_vars[j]].as_long() for j in range(num_buttons)])
        min_presses.append(total_presses)
    # if there is no solution
    else:
        min_presses.append(float('inf'))

print(sum(min_presses))