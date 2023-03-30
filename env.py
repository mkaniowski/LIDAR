import numpy as np
import pygame

class buildEnv:
    def __init__(self, mapDim):
        pygame.init()
        self.points = []
        self.externalMap = pygame.image.load('map.png')
        self.mapH, self.mapW = mapDim
        pygame.display.set_caption('LIDAR')
        self.map = pygame.display.set_mode((self.mapH, self.mapW))
        self.map.blit(self.externalMap, (0, 0))
    
    def poalr2cart(self, dist, angle, pos):
        x = dist * np.cos(angle) + pos[0]
        y = -dist * np.sin(angle) + pos[1]
        return int(x), int(y)
    
    def dataStorage(self, data):
        print(len(self.points))
        for ele in data:
            point = self.poalr2cart(ele[0], ele[1], ele[2])
            if point not in self.points:
                self.points.append(point)

    def showData(self):
        self.infomap = self.map.copy()
        for point in self.points:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))