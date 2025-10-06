import pygame
from circleshape import CircleShape
from constants import *

class Shoot(CircleShape):
    containers = ()

    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        # default velocity; Player.shoot will set it
        self.velocity = pygame.Vector2(0, 0)

        # auto-add to groups assigned from main.py
        for g in self.containers:
            g.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255, 255, 255), center, int(self.radius))
