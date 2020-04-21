# https://colab.research.google.com/drive/1lo8pAAo5GiUk4BZvSEnnkET6hTjP6eLR?fbclid=IwAR2Neo8mTcS0Nwcyvbu8YHo0qcY28MK1ScEEy1WZsJ6g7fLeuvvxD31ivgg#scrollTo=xMlr5rvpUtXr
# Matplotlib 시작하기

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 500)
y = x**2

plt.plot(x, y)
plt.title("Square function")
plt.xlabel("x")
plt.ylabel("y = x**2")
plt.grid(True)
plt.show()