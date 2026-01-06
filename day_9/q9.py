import numpy as np

def line_intersects_rectangle(p1, p2, rect_p1, rect_p2):
    # normalize rectangle corners to min/max
    min_x = np.min([rect_p1[0], rect_p2[0]])
    max_x = np.max([rect_p1[0], rect_p2[0]])
    min_y = np.min([rect_p1[1], rect_p2[1]])
    max_y = np.max([rect_p1[1], rect_p2[1]])
    
    # checks if both x coordinates are on one side of the rectangle.
    if (p1[0] <= min_x and p2[0] <= min_x) or (p1[0] >= max_x and p2[0] >= max_x):
        return False
    
    # checks if both y coordinates are on one side of the rectangle.
    if (p1[1] <= min_y and p2[1] <= min_y) or (p1[1] >= max_y and p2[1] >= max_y):
        return False
    
    # if we get here, it means the line passes through the rectangle.
    return True

points = []
with open('day_9/input.txt', 'r') as f:

    while True:
        line = f.readline().strip()
        if not line:
            break
        points.append(tuple(int(x) for x in line.split(',')))

points = np.array(points)
differences = np.diagonal(np.subtract.outer(points, points), axis1=1, axis2=3)
areas = np.prod(np.abs(differences) + 1, axis=2)

# loop through areas, starting from maximum and going downwards.
track = 0
while True:
    # find the remaining rectangle with the largest area
    idxs = np.unravel_index(areas.argmax(), areas.shape)
    rect_p1 = points[idxs[0]]
    rect_p2 = points[idxs[1]]

    # loop through all the lines and see if any intersect with this rectangle,
    # if not, we found the largest valid rectangle.
    valid_rectangle = True
    for i in range(points.shape[0]):
        p1 = points[i]
        p2 = points[i+1] if i+1 < len(points) else points[0]

        # check if these intersect with the rectangle defined by rect_p1 and rect_p2
        # if they do, mark as invalid and break.

        if line_intersects_rectangle(p1, p2, rect_p1, rect_p2):
            valid_rectangle = False
            areas[idxs] = -1
            areas[idxs[::-1]] = -1
            break

    if valid_rectangle:
        print(f'part 2: {areas[idxs]}')
        break

