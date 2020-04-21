# https://colab.research.google.com/drive/1lo8pAAo5GiUk4BZvSEnnkET6hTjP6eLR?fbclid=IwAR2Neo8mTcS0Nwcyvbu8YHo0qcY28MK1ScEEy1WZsJ6g7fLeuvvxD31ivgg#scrollTo=xMlr5rvpUtXr
# 스타일 지정

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.4, 1.4, 30)
line1, line2, line3 = plt.plot(x, x, 'g--', x, x**2, 'r:', x, x**3, 'b^')
line1.set_linewidth(3.0)
line1.set_dash_capstyle("round")
line3.set_alpha(0.2)
plt.show()