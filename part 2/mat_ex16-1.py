import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)
l = plt.plot(t, s)

ax = plt.axis([0,TWOPI,-1,1])

redDot, = plt.plot([0], [np.sin(0)], 'ro')

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
                                      interval=10, blit=True, repeat=True)
myAnimation.save('ex16-1.gif', writer='imagemagick', fps=30, dpi=100)
plt.show()

1. Matplotlib 시작하기
2. 스타일 지정 (style)
3. 저장 (save)
4. 부분 그래프 (subplot)
5. 여러 그래프 (figure)
6. 텍스트
7. 범례(legends)
8. 비선형 척도
9. 틱과 티커
10. 극좌표계 투영
11. 3차원 투영
12. 산점도
13. 선
14. 히스토그램
15. 이미지
16. 애니메이션
17. 애니메이션 비디오 저장