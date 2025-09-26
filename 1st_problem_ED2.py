import numpy as np
import matplotlib.pyplot as plt

# Different values of v
v = np.linspace(0.0000001, 0.999999999, 2000)

# Define y = 10v as the electric field in one dimension is 10*x as we plot the gradient of electric field
y = 10 * v

# Plotting
plt.plot(v, y, label='y = 10v')
plt.xlabel('v')
plt.ylabel('10v')
plt.title('Plot of difference between galilean and lorentz vs velocity of particle')
plt.legend()
plt.grid(True)
plt.show()
