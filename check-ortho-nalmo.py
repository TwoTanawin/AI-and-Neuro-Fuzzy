import numpy as np

# Define the vectors as rows in a 2D NumPy array
vectors = np.array([
    [1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1],
    [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1],
    [1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1]
])

# Check if each vector is orthogonal
are_orthogonal = []

for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
        dot_product = np.dot(vectors[i], vectors[j])
        are_orthogonal.append(f"Vector {i + 1} and Vector {j + 1} are orthogonal: {dot_product == 0}")

# Check if each vector is orthonormal
are_orthonormal = []

for i in range(len(vectors)):
    norm = np.linalg.norm(vectors[i])
    are_orthonormal.append(f"Vector {i + 1} is orthonormal: {np.allclose(norm, 1)}")

# Print the results
for result in are_orthogonal:
    print(result)

for result in are_orthonormal:
    print(result)
