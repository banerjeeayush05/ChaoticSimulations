import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

SIGMA = 10.0
BETA = 8.0 / 3.0
RHO = 28.0

NUM_POINTS = 10000

x = 0.01
y = 0.0
z = 0.0

x_points = np.array([])
y_points = np.array([])
z_points = np.array([])

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

def animate(num, data, line):
   line.set_color((0, 0, 0))
   line.set_alpha(0.7)
   line.set_data(data[0:2, :num])
   line.set_3d_properties(data[2, :num])
   return line

for i in range(NUM_POINTS):
    dt = 0.01
    dx = SIGMA * (y - x) * dt
    dy = (x * (RHO - z) - y) * dt
    dz = (x * y - BETA * z) * dt

    x += dx
    y += dy
    z += dz

    x_points = np.append(x_points, x)
    y_points = np.append(y_points, y)
    z_points = np.append(z_points, z)

data = np.array([x_points, y_points, z_points])

print(x_points)

fig = plt.figure()
ax = Axes3D(fig)
ax.autoscale(tight = True)

line, = plt.plot(data[0], data[1], data[2], lw=1, c='red')
line_ani = animation.FuncAnimation(fig, animate, frames = NUM_POINTS, fargs=(data, line), interval=50, blit=False)

plt.show()