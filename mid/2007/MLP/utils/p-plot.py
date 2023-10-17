import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
scatter = ax.scatter(x, y, z, c=colors, marker='o', label='Points')

# Define the decision boundary
boundary_x = [p1[0], p4[0]]
boundary_y = [p1[1], p4[1]]
boundary_z = [p1[2], p4[2]]

# Plot the decision boundary as a line
# ax.plot(boundary_x, boundary_y, boundary_z, c='g', linestyle='--', label='Decision Boundary')

# Annotate the points with their coordinates and associated t values
for i, point in enumerate(points):
    ax.text(point[0], point[1], point[2], f'p{i + 1}\n t{i + 1}={eval(f"t{i + 1}")}', fontsize=10, color='black')

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Display the plot
plt.legend()
plt.show()
