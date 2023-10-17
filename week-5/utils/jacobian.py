import numpy as np

t = np.array([2, 8, 8, 20])  # Target
s_layer2 = np.array([-0.1247, -0.1711, -0.1144, -0.1552, -0.0937, -0.0914, -0.0699, -0.0413])
n_layer1 = np.array([0.475, 0.4256, 0.3543, 0.6682, 0.2497, 0.8455, 0.168, 0.937])
bias = np.array([-1])
p = np.array([5, 10, 15, 20])
# Create a 4x7 matrix filled with zeros
matrix = np.zeros((4, 7))

# Fill in the values based on the pattern described
for i in range(len(t)):
    matrix[i, 0] = s_layer2[i * 2]*p[i]
    matrix[i, 1] = s_layer2[i * 2]
    matrix[i, 2] = s_layer2[i * 2 + 1]*p[i] 
    matrix[i, 3] = s_layer2[i * 2 + 1]
    matrix[i, 4] = bias * n_layer1[i * 2]
    matrix[i, 5] = bias * n_layer1[i * 2 + 1]
    matrix[i, 6] = bias

# Print the resulting 4x7 matrix
print(matrix)
