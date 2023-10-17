# Define your 4x4 matrix as a nested list
matrix = [
    [1.087, 0.010, 0.090, 1.851],
    [0.090, 0.010, 0.150, 0.193],
    [1.851, 0.150, 3.516, 0.010],
    [2.235, 0.193, 4.159, 5.000]
]

# Add 0.01 to each element in the matrix
for i in range(4):
    for j in range(4):
        matrix[i][j] += 0.01

# Print the updated matrix
for row in matrix:
    print(row)
