import pygame
from pygame.sprite import Sprite

class Bullet_settings:
     def __init__(self):
        self.width = 1.5
        self.height = 15
        self.speed_factor = 3.5
        self.color = (250, 0, 0)
class Bullet(Sprite):
    #A class to manage the bullets
    def __init__(self, Bullet_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.bulset = Bullet_settings

        self.rect = pygame.Rect(0, 0, self.bulset.width,
                self.bulset.height)
        self.rect.centerx = ship.rect.centerx
        self.center = self.rect.centerx
        self.rect.top = ship.rect.top
        self.rect2 = self.rect
        self.y = float(self.rect.y)
        self.color = self.bulset.color
        self.speed_factor = self.bulset.speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.rect2.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def doubler(self):
        self.rect.centerx = self.center + 1.5
        self.rect2.centerx = self.center - 1.5
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)

    def machinegun(self):
        self.speed_factor *= 2;

    def doublemachine(self):
        self.speed_factor *= 2;
        doubler()
