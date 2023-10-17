import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the points
p1 = [0, 0, 0]
p2 = [0, 0, 1]
p3 = [0, 1, 0]
p4 = [0, 1, 1]
p5 = [1, 0, 0]
p6 = [1, 0, 1]
p7 = [1, 1, 0]
p8 = [1, 1, 1]

# Define the associated values
t1 = 1
t2 = 0
t3 = 0
t4 = 1
t5 = 0
t6 = 1
t7 = 1
t8 = 0

# Extract x, y, and z coordinates of all points
points = [p1, p2, p3, p4, p5, p6, p7, p8]
x = [point[0] for point in points]
y = [point[1] for point in points]
z = [point[2] for point in points]

# Plot the points with different colors based on associated values
colors = ['r' if t == 1 else 'b' for t in [t1, t2, t3, t4, t5, t6, t7, t8]]
scatter = ax.scatter(x, y, z, c=colors, marker='o')
legend_labels = ['Point with t=1', 'Point with t=0']
ax.legend(handles=scatter.legend_elements()[0], labels=legend_labels)

# Define the range for the dynamic decision boundary
boundary_x_range = np.linspace(0, 1, 100)
boundary_y_range = np.linspace(0, 1, 100)
boundary_x, boundary_y = np.meshgrid(boundary_x_range, boundary_y_range)

# Calculate the dynamic decision boundary based on t values
t_boundary = (t1 + t4) / 2  # You can change this logic based on your specific criteria

# Create a 3D surface for the decision boundary
boundary_z = np.full(boundary_x.shape, t_boundary)

# Plot the dynamic decision boundary as a surface
ax.plot_surface(boundary_x, boundary_y, boundary_z, cmap='viridis', alpha=0.5, label='Dynamic Decision Boundary')

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Display the plot
plt.show()
