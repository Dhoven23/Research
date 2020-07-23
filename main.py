import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import style

from Data.Particle import Particle


def generate(n_particles, grid_size):
    X = np.arange(0, grid_size, 1)
    Y = np.arange(0, grid_size, 1)
    return [Particle(
        [
            float(np.random.normal(0, 1, 1)),
            float(np.random.normal(0, 1, 1)),
        ],
        [
            int(np.random.normal(50, 20, 1)),
            int(np.random.normal(50, 20, 1)),
        ],
        int(np.random.normal(10, 0.5, 1)),
        grid_size,
        np.meshgrid(X, Y)
    ) for _ in range(n_particles)]


def particleGen():
    global particles
    particles = generate(10, 100)


def Iterate():
    Z = np.zeros((100, 100))
    global particles
    for p in particles:
        p.iterate(1)
        Z = np.add(Z, p.Zmap)
    return Z


def animate(i):
    Z = Iterate()
    X, Y = np.meshgrid(np.arange(0, 100, 1), np.arange(0, 100, 1))
    axis.clear()
    surf = axis.plot_surface(X, Y, Z,
                             cmap="viridis")
    axis.set_zlim(0, 6)


style.use('fivethirtyeight')
fig = plt.figure()
axis = fig.gca(projection='3d')

particleGen()
anim = FuncAnimation(fig, animate,
                     frames=1000,
                     interval=20)

anim.save('test.mp4', writer='ffmpeg', fps=30)
