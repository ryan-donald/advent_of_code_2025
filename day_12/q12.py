# input in format:
# {index}:
# ###
# ##.
# .##

# {x}x{y}: indecies of shapes that are in the area.

# shape format, # = filled, . = empty.
# shapes can be rotated and flipped.

# shapes can fit together but not overlap

# must find if the shapes given for an area can fit together in that area

shapes = []
areas = []

count = 0
with open('day_12/input.txt', 'r') as f:

    while True:
        line = f.readline().strip()

        if not line:
            count += 1
            if count > 6:
                break
            continue
        
        if count < 6:
            if line.endswith(':'):
                current_shape = []
            else:
                current_shape.append(line)
                if len(current_shape) == 3:
                    shapes.append(current_shape)

        else:
            parts = line.split(':')
            dimensions = [int(x) for x in parts[0].split('x')]
            indecies = [int(x) for x in parts[1].strip().split(' ')]

            areas.append((dimensions, indecies))

print(f'shapes: {shapes}')
# print(f'areas: {areas}')

shape_areas = []

for shape in shapes:
    area = 0
    for row in shape:
        for char in row:
            if char == '#':
                area += 1
    shape_areas.append(area)

# print(shape_areas)
        
count = 0

for area in areas:
    dimensions = area[0]
    indecies = area[1]

    total_area = dimensions[0] * dimensions[1]

    shapes_area = 0
    for idx, val in enumerate(indecies):
        shapes_area += val*shape_areas[idx]

    if shapes_area <= total_area:
        # print('fits')
        count+=1
    # else:
        # print('does not fit')
            
print(count)