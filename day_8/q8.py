import numpy as np

positions = []

with open('day_8/input.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        coords = line.split(',')
        positions.append(list(float(c) for c in coords))

# print(positions)

# convert to numpy array
positions = np.array(positions, dtype=float)
print(positions.shape)

# compute pairwise distances
subtracted = np.diagonal(np.subtract.outer(positions, positions), axis1=1, axis2=3)

# compute euclidean distances
distances = np.linalg.norm(subtracted, axis=2)

# make self-distances very large
np.fill_diagonal(distances, 9999999999)


# finds the two closest boxes iteratively.
# to build and store each of the circuits, 
# use a set. Each time we find a pair, add both to the set.
# if one is already in a set, add the other to that set.
# lastly, if one is in one set, and another is in another set,
# merge the two sets.

circuits = []

i = 0
num_circuits = 1
num_boxes = len(positions)
while num_circuits < num_boxes:

    # find minimum distance for each point
    min_distances = np.min(distances, axis=1)

    first_box = np.argmin(min_distances)
    # print(f'first_box: {first_box}, position: {positions[first_box]}')
    second_box = np.argmin(distances[first_box])
    # print(f'second_box: {second_box}, position: {positions[second_box]}')

    distances[first_box][second_box] = 9999999999
    distances[second_box][first_box] = 9999999999

    # creates the first circuit
    if i == 0:
        circuits.append(set([first_box, second_box]))
        # print(circuits)

    # every other pair
    else:
        # check if either box is already in a set.
        found = False
        first_circuit = None

        # iterate through existing circuit
        for circuit in circuits:
            # if either box is in the circuit
            if (first_box in circuit) or (second_box in circuit):
                # check if both boxes are in different circuits
                # store the first circuit we find
                found = True
                if first_circuit == None:
                    first_circuit = circuit

                # if both boxes are in different circuits, merge the circuits
                else:
                    # merge sets
                    first_circuit.update(circuit)
                    circuits.remove(circuit)
                    break
                
                # if only one box is in the circuit, add the other box to the circuit
                circuit.add(first_box)
                circuit.add(second_box)
        
        # if neither box is in a circuit, append a new circuit
        if not found:
            circuits.append(set([first_box, second_box]))

    num_circuits = len(circuits[0])
    i += 1