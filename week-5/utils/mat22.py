import numpy as np

def convert_to_desired_matrix(original_array):
    row, col = original_array.shape  # Remove the parentheses
    # Calculate the desired values for the diagonal elements
    diagonal_values = [(1 - original_array[i][0]) * original_array[i][0] for i in range(row)]

    # Create the 3x3 desired matrix with diagonal values
    desired_matrix = np.diag(diagonal_values)
        
    return desired_matrix

