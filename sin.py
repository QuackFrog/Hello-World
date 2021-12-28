import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.savefig('sin.png')
