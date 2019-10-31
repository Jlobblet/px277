"""Given three position vectors of objects exerting a force on each
other according to Hook's law, i.e. force proportional to distance,
calculate the total internal force for each particle from all others.

Set the proportionality constant to k=1 and print all three force
vectors.
The position vectors are `[1,0,0], [0,1,0], [0,0,1]`. In algebra, this
force expression would be F_j = k∑Ni≠j r_i−r_j.
"""
import numpy as np

k = 1
positions = [
    np.array([1.0, 0.0, 0.0]),
    np.array([0.0, 1.0, 0.0]),
    np.array([0.0, 0.0, 1.0]),
]

forces = [
    k
    * np.sum(
        [
            positions[i] - positions[j]
            for i in range(len(positions))
            if i != j
        ],
        axis=0,
    )
    for j in range(len(positions))
]
[print(force) for force in forces]
