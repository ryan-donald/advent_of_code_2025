

with open("day_2/input.txt") as f:
    input = f.readline()

id_ranges = input.strip().split(',')

invalid_ids = []

# part 1
for bounds in id_ranges:
    bounds = bounds.split('-')
    
    for i in range(int(bounds[0]), int(bounds[1]) + 1):
        i_str = str(i)
        len_i = len(i_str)
        # cannot be an invalid id if not even length
        if len_i%2 != 0:
            continue
        
        first_half = i_str[:len_i//2]
        second_half = i_str[len_i//2:]

        if first_half == second_half:
            invalid_ids.append(i)

print(sum(invalid_ids))

# part 2

invalid_ids = []

for bounds in id_ranges:
    bounds = bounds.split('-')
    
    for i in range(int(bounds[0]), int(bounds[1]) + 1):
        i_str = str(i)
        len_i = len(i_str)
        
        candidate_substr = ""
        
        for idx, char in enumerate(i_str):
            if idx > (len_i // 2) - 1:
                break

            candidate_substr += char

            if len_i % len(candidate_substr) != 0:
                continue

            repetitions = len_i // len(candidate_substr)
            if candidate_substr * repetitions == i_str:
                invalid_ids.append(i)
                break

print(sum(invalid_ids))

            
            

            