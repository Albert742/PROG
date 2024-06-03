import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r1 = 1
r2 = 2
theta = np.linspace(0, 2*np.pi, 100)
z = np.linspace(0, 2*np.pi, 100)
theta, z = np.meshgrid(theta, z)
x = r1 * np.cos(theta) + r2 * np.cos(z)
y = r1 * np.sin(theta) + r2 * np.sin(z)

surface = ax.plot_surface(x, y, z, alpha=0.5)

def update(frame):
    surface.remove()
    z = frame * np.linspace(0, 2*np.pi, 100)
    theta, z = np.meshgrid(theta, z)
    x = r1 * np.cos(theta) + r2 * np.cos(z)
    y = r1 * np.sin(theta) + r2 * np.sin(z)
    surface = ax.plot_surface(x, y, z, alpha=0.5)
    return surface,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 100, 100), interval=50, blit=True)
plt.show()