# import numpy as np
# import matplotlib.pyplot as plt

# # Define the time values for the plot
# t = np.linspace(0, 10, 500)  # Time range from 0 to 10 seconds

# # Calculate the current values using the expression
# i = (1/4) * np.exp(-25/20 * t) + (3/4) * np.exp(-20/50 * t)

# # Plotting
# plt.figure(figsize=(8, 6))
# plt.plot(t, i, label=r'$i(t) = \frac{1}{4} e^{-\frac{25}{20} t} + \frac{3}{4} e^{-\frac{20}{50} t}$')
# plt.xlabel('Time (s)')
# plt.ylabel('Current (A)')
# plt.title('Current vs. Time')
# plt.legend()
# plt.grid()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the time values
t = np.linspace(0, 5, 500)  # Time values from 0 to 5 seconds

# Calculate the current values using the expression
I = -5/36 * np.exp(-11 * t)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(t, I, label=r'$I(t) = -\frac{5}{36} e^{-11t}$')
plt.xlabel('Time (seconds)')
plt.ylabel('Current (I)')
plt.title('Exponential Decay of Current')
plt.legend()
plt.grid()
plt.show()
