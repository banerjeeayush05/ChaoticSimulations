import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import math

DT = 0.01
COLORS = ["black"]
SIMULATION_TYPE = 0
TRANSFORM_TYPE = 4
ROTATE: bool = False

def lorenzUpdate(x, y, z):
    SIGMA = 10.0
    BETA = np.full(x.shape[0], 8.0 / 3.0)
    RHO = 28.0

    dx = SIGMA * (y - x) * DT
    dy = (x * (RHO - z) - y) * DT
    dz = (x * y - BETA * z) * DT   

    return dx, dy, dz

def aizawaUpdate(x, y, z):
    ALPHA = 0.95
    BETA = np.full(x.shape[0], 0.7)
    GAMMA = np.full(x.shape[0], 0.6)
    DELTA = 3.5
    EPSILON = 0.25
    PHI = 0.1

    dx = (x * (z - BETA) - DELTA * y) * DT
    dy = (DELTA * x + y * (z - BETA)) * DT
    dz = (GAMMA + ALPHA * z - np.power(z, 3) / 3 - (np.power(x, 2) + np.power(y, 2)) * (1 + EPSILON * z) + PHI * z * np.power(x, 3)) * DT

    return dx, dy, dz

def halvorsenUpdate(x, y, z):
    ALPHA = 1.4

    dx = ((-ALPHA * x - 4 * y - 4 * z - np.power(y, 2))) * DT
    dy = ((-ALPHA * y - 4 * z - 4 * x - np.power(z, 2))) * DT
    dz = ((-ALPHA * z - 4 * x - 4 * y - np.power(x, 2))) * DT

    return dx, dy, dz

def financeUpdate(x, y, z):
    ALPHA = 0.001
    BETA = 0.2
    GAMMA = 1.1

    dx = ((1 / BETA - ALPHA) * x + z + x * y) * DT
    dy = (-BETA * y - np.power(x, 2)) * DT
    dz = (-x - GAMMA * z) * DT

    return dx, dy, dz

def nosehooverUpdate(x, y, z):
    ALPHA = np.full(x.shape[0], 1.5)

    dx = y * DT
    dy = (-x + y * z) * DT
    dz = (ALPHA - np.power(y, 2)) * DT

    return dx, dy, dz

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

x_points = np.array([[1]], dtype = float)
y_points = np.array([[1]], dtype = float)
z_points = np.array([[1]], dtype = float)

count = 0
def update(frame):
    ax.clear()
    # ax.set_axis_off()

    if(ROTATE):
        global count
        if(count == 4):
            ax.view_init(0, frame % 360)
            count = 0
        else:
            count += 1

    global x_points, y_points, z_points
    x = x_points[0: x_points.shape[0], x_points.shape[1] - 1]
    y = y_points[0: y_points.shape[0], y_points.shape[1] - 1]
    z = z_points[0: z_points.shape[0], z_points.shape[1] - 1]

    if(TRANSFORM_TYPE == 0):
        window_view = 25
        x_buffer = 0
        y_buffer = -20
        z_buffer = 0
        dx, dy, dz = lorenzUpdate(x, y, z)
    elif(TRANSFORM_TYPE == 1):
        window_view = 2
        x_buffer = 0
        y_buffer = 0
        z_buffer = 0
        dx, dy, dz = aizawaUpdate(x, y, z)
    elif(TRANSFORM_TYPE == 2):
        window_view = 50
        x_buffer = 0
        y_buffer = 0
        z_buffer = 0
        dx, dy, dz = halvorsenUpdate(x, y, z)
    elif(TRANSFORM_TYPE == 3):
        window_view = 5
        x_buffer = 0
        y_buffer = 0
        z_buffer = 0
        dx, dy, dz = financeUpdate(x, y, z)
    elif(TRANSFORM_TYPE == 4):
        window_view = 5
        x_buffer = 0
        y_buffer = 0
        z_buffer = 0
        dx, dy, dz = nosehooverUpdate(x, y, z)

    ax.axes.set_xlim3d(left = -(window_view + x_buffer), right = window_view - x_buffer) 
    ax.axes.set_ylim3d(bottom = -(window_view + y_buffer), top = window_view - y_buffer) 
    ax.axes.set_zlim3d(bottom = -(window_view + z_buffer), top = window_view - z_buffer)

    x_points = np.append(x_points, (x + dx).reshape((x + dx).shape[0], 1), axis = 1)
    y_points = np.append(y_points, (y + dy).reshape((y + dy).shape[0], 1), axis = 1)
    z_points = np.append(z_points, (z + dz).reshape((z + dz).shape[0], 1), axis = 1)

    if(SIMULATION_TYPE == 0):
        for i in range(x.shape[0]):
            for j in range(len(COLORS)):
                if(i >= j * x.shape[0] / len(COLORS) and i < (j + 1) * x.shape[0] / len(COLORS)):
                    ax.plot(x_points[i], y_points[i], z_points[i], color = COLORS[j], linewidth = 1)
                    break
    elif(SIMULATION_TYPE == 1):
        for i in range(x.shape[0]):
            for j in range(len(COLORS)):
                if(i >= j * x.shape[0] / len(COLORS) and i < (j + 1) * x.shape[0] / len(COLORS)):
                    ax.scatter(x_points[i, x_points.shape[1] - 1], y_points[i, y_points.shape[1] - 1], z_points[i, z_points.shape[1] - 1], color = COLORS[j], s = 5)
                    break
    elif(SIMULATION_TYPE == 2):
        for i in range(x.shape[0]):
            for j in range(len(COLORS)):
                if(i >= j * x.shape[0] / len(COLORS) and i < (j + 1) * x.shape[0] / len(COLORS)):
                    ax.scatter(x_points[i], y_points[i], z_points[i], color = COLORS[j], s = 5)
                    break
        
ani = FuncAnimation(fig, update, interval = 10, repeat = False)
plt.show()