import pygame
import numpy as np

class LaserSensor:
    def __init__(self, range, map, noise):
        self.range = range
        self.noise = np.array([noise[0], noise[1]])
        self.pos = (0, 0)
        self.map = map
        self.w, self.h = pygame.display.get_surface().get_size()
        self.obstacles = []

    def dist(self, obstacle):
        return np.linalg.norm(np.array(obstacle) - np.array(self.pos))
    
    def detect(self):
        data = []
        x1, y1 = self.pos
        for angle in np.linspace(0, 2*np.pi, 360, False):
            x2, y2 = (x1 + self.range * np.cos(angle), y1 - self.range * np.sin(angle))
            for i in range(100):
                u = i/100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.w and 0 < y < self.h:
                    color = self.map.get_at((x, y))
                    if color == (0, 0, 0):
                        distance = self.dist((x, y))
                        out = whiteNoise(distance, angle, self.noise)
                        out.append(self.pos)
                        data.append(out)
                        break
        if len(data) > 0:
            return data
        else:
            return []


def whiteNoise(dist, angle, sigma):
    mean = np.array([dist, angle])
    cov = np.diag(sigma**2)
    dist, angle = np.random.multivariate_normal(mean, cov)
    angle = max(angle, 0)
    return [dist, angle]