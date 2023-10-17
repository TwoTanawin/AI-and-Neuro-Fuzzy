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
scatter = ax.scatter(x, y, z, c=colors, marker='o')

# Annotate the points with their coordinates and associated t values
for i, point in enumerate(points):
    ax.text(point[0], point[1], point[2], f'p{i + 1}\n t{i + 1}={eval(f"t{i + 1}")}', fontsize=10, color='black')

# Create vectors for p and t
p_vectors = [(x[i], y[i], z[i]) for i in range(len(points))]
t_vectors = [(0, 0, eval(f't{i + 1}')) for i in range(len(points))]

# Plot vectors
for p_vector, t_vector in zip(p_vectors, t_vectors):
    ax.quiver(p_vector[0], p_vector[1], p_vector[2], t_vector[0], t_vector[1], t_vector[2], color='gray', alpha=0.5)

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Display the plot
plt.show()
