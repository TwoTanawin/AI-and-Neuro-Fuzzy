import numpy as np
from sympy import symbols, Eq, solve

# Define symbolic variable
bias = symbols('bias')

# Define NumPy arrays for w and p
w = np.array([-1, -2])
p = np.array([3, 8])

# Create the equation
eqn = Eq(np.dot(w, p) + bias, 0)

# Solve for bias
solutions = solve(eqn, bias)
print(solutions)
