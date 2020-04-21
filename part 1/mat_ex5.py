import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.4, 1.4, 30)

plt.figure(1)
plt.subplot(211)
plt.plot(x, x**2)
plt.title("Square and Cube")
plt.subplot(212)
plt.plot(x, x**3)

plt.figure(2, figsize=(10, 5))
plt.subplot(121)
plt.plot(x, x**4)
plt.title("y = x**4")
plt.subplot(122)
plt.plot(x, x**5)
plt.title("y = x**5")

plt.figure(1)      # 그림 1로 돌아변경하여, 활성화된 부분 그래프는 212 (하단)이 됩니다
plt.plot(x, -x**3, "r:")

plt.show()