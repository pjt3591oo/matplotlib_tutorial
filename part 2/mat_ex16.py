import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc('animation', html='jshtml')

x = np.linspace(-1, 1, 100)
y = np.sin(x**2*25)
data = np.array([x, y])

fig = plt.figure()
line, = plt.plot([], [], "r-") # start with an empty plot
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.plot([-0.5, 0.5], [0, 0], "b-", [0, 0], [-0.5, 0.5], "b-", 0, 0, "ro")
plt.grid(True)
plt.title("Marvelous animation")

# this function will be called at every iteration
def update_line(num, data, line):
    line.set_data(data[..., :num] + np.random.rand(2, num) / 25)  # we only plot the first `num` data points.
    return line,

line_ani = animation.FuncAnimation(fig, update_line, frames=100, fargs=(data, line), interval=67)
# plt.close()
# plt.show()
line_ani
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
line_ani.save('my_wiggly_animation.mp4', writer=writer)
