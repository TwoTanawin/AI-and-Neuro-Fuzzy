# import numpy as np

# # Create a 7x7 identity matrix
# matrix = np.eye(7)

# # Set the diagonal elements to 0.5
# matrix *= 0.5

# print(matrix)

import numpy as np

def create_matrix(size, diagonal_value):
    # Create a size x size identity matrix
    matrix = np.eye(size)
    
    # Set the diagonal elements to the specified value
    matrix *= diagonal_value
    
    return matrix

# Usage example
size = 7
diagonal_value = 0.5
result_matrix = create_matrix(size, diagonal_value)

print(result_matrix)
