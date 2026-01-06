from collections import defaultdict, deque

connections = defaultdict(list)
queue = deque()

with open('day_11/input.txt') as f:
    
    while True:
        line = f.readline().strip()

        if not line:
            break

        parts = line.split(': ')
        key = parts[0]
        parts = parts[1].split(' ')

        connections[key] = parts

# start with 'you' as a path containing just the starting node
queue.append(['you'])

count = 0

while queue:
    current_path = queue.popleft()
    current_node = current_path[-1]
    
    # get next devices connected to the current node
    for next_device in connections[current_node]:
        if next_device == 'out':
            count += 1
        
        # check if device has been visited in this path before
        elif next_device not in current_path:
            new_path = current_path + [next_device]
            queue.append(new_path)

print(f'part 1: {count}')


# connections = dictionary, key: device, value: list of connected devices
# part 2

# my soltution to part 1 was a BFS that tracked the paths to avoid cycles, but was very inefficient for part 2.

# more efficient solution is to use dfs with caching. Two variables track whether dac or fft is within the current path.

cache = defaultdict(int)

def dfs(device, found_dac, found_fft):
    # base case, return 1 if output and both dac and fft in path
    if device == 'out':
        return 1 if found_dac and found_fft else 0
    
    # check if this state has been computed before
    if (device, found_dac, found_fft) in cache:
        return cache[(device, found_dac, found_fft)]
    
    # recursive case exploring connections
    cache[(device, found_dac, found_fft)] = sum(
        dfs(next_device, found_dac or next_device == 'dac', found_fft or next_device == 'fft')
        for next_device in connections[device]
    )
    return cache[(device, found_dac, found_fft)]

# start dfs from 'you' with neither dac nor fft found
part2_count = dfs('svr', False, False)
print(f'part 2: {part2_count}')

