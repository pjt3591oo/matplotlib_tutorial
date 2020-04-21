import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.4, 1.4, 30)
plt.plot(x, x**2)
plt.savefig("mung.png", transparent=True)