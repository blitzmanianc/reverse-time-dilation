import numpy as np
import matplotlib.pyplot as plt

c = 3e8

def time_dilation(v):
    gamma = 1 / np.sqrt(1 - (v**2 / c**2))
    return gamma

velocities = np.linspace(0, 0.99 * c, 1000)

time_dilations = time_dilation(velocities)

plt.figure(figsize=(10,6))
plt.plot(velocities/ c, time_dilations, label = 'Time Dilation Factor')
plt.title('Time Dilation as a Function of Velocity')
plt.xlabel('Velocity (as a fraction of the speed of light, c)')
plt.ylabel('Time Dilation Factor (γ)')
plt.grid(True)
plt.legend()
plt.show()

