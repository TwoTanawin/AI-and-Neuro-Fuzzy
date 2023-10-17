import numpy as np

# Define the matrix 'a'
a = np.array([[-1, 1],
              [0, -2]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(a)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
