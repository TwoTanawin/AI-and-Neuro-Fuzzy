import matplotlib.pyplot as plt

# Define the data points
a1 = [14, 16]
a2 = [20, 10]
a3 = [18, 6]
a4 = [8, 4]
a5 = [6, 10]

# Extract x and y values for each point
x_values = [a1[0], a2[0], a3[0], a4[0], a5[0]]
y_values = [a1[1], a2[1], a3[1], a4[1], a5[1]]

# Create a scatter plot
plt.scatter(x_values, y_values, marker='o', label='Points')

# Add labels to the points
for i, (x, y) in enumerate(zip(x_values, y_values)):
    plt.text(x, y, f'a{i+1} ({x},{y})')

# Add labels to the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
