import numpy as np
import pygame

class Balloon:
    def __init__(self, screen_width):
        self.x = np.random.randint(50, screen_width - 50)
        self.y = 0
        self.speed = np.random.randint(2, 6)
        self.radius = 20
        self.color = (255, 0, 0)

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        dist = np.sqrt((self.x - pos[0])**2 + (self.y - pos[1])**2)
        return dist < self.radius