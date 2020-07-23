import numpy as np
from numpy import exp


class Particle:
    def __init__(self, velocity, position, mass, bound, grid):
        self.Velocity = velocity
        self.Position = position
        self.bound = bound
        self.Mass = mass
        self.grid = grid
        self.Zmap = 4 * exp((-mass) * ((grid[0] - position[0]) ** 2 + (grid[1] - position[1]) ** 2))

    def iterate(self, dt):

        for i in range(0, len(self.Position)):
            if ((int(self.Position[i]) + int(self.Velocity[i]) * dt) < 0) | ((int(self.Position[i]) + int(self.Velocity[i]) * dt) > self.bound):
                self.Velocity[i] *= -1
        self.Position = np.add(self.Position, self.Velocity * dt)
        self.Zmap =exp(
            (-self.Mass**-1) * ((self.grid[0] - self.Position[0]) ** 2 + (self.grid[1] - self.Position[1]) ** 2))
