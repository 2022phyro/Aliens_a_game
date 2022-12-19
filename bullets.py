import pygame
from pygame.sprite import Sprite
from Alien_combo import ALIEN as A
from Drawing import *
from threading import Timer
import time
class Bullet_settings:
     def __init__(self):
        self.width = 1.5
        self.height = 15
        self.color = (250, 0, 0)
        self.doublegun = 25
        self.s_scale = 1.1
        self.dynamic_settings()
     def dynamic_settings(self):
        self.speed_factor = 3.5
        self.a_speed_factor = 0.5
     def speedup(self):
         # self.speed_factor *= self.s_scale
         self.a_speed_factor *= self.s_scale

class Bullet(Sprite):
    #A class to manage the bullets
    def __init__(self, Bullet_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.doubles = 0
        self.ship = ship
        self.gme = Screen_settings()
        self.bulset = Bullet_settings
        self.rect = pygame.Rect(0, 0, self.bulset.width,
                self.bulset.height)
        self.rect.centerx = ship.rect.centerx
        self.center = self.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = self.bulset.color
        self.rect2 =  pygame.Rect(0, 0, self.bulset.width,
                self.bulset.height)
        self.rect2.centerx = ship.rect.centerx
        self.rect2.top = ship.rect.top
       
        self.speed_factor = self.bulset.speed_factor
        self.doublegun = self.bulset.doublegun

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.rect2.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    def draw_bullets(self, bullets, idx=0):
        for bullet in bullets.sprites():
            if idx == 1:
                bullet.doubler()
            # bullet.machinegun()
            bullet.draw_bullet()
    def doubler(self):
        self.rect.centerx = self.center + self.doublegun
        self.rect2.centerx = self.center - self.doublegun
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)


    def machinegun(self):
        self.speed_factor += 2

    def move_bullets(self, event, bullets):
        if event.key == pygame.K_SPACE :
            new_bullet = Bullet(self.bulset, self.screen, self.ship)
            bullets.add(new_bullet)

    def rid_excess_bullets(self, bullets):
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

    def update_the_catridge(self, bullets, aliens):
        bullets.update()
        self.rid_excess_bullets(bullets)

class Alien_bullet(Sprite):
    def __init__(self, Bullet_settings, screen, ship):
        super(Alien_bullet, self).__init__()
        self.screen = screen
        self.ship = ship
        self.bulset = Bullet_settings
        self.rect = pygame.Rect(0, 0, self.bulset.width,
                                self.bulset.height)
        self.rect.centerx = ship.rect.centerx
        self.center = self.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = (0, 255, 255)
        self.rect2 = pygame.Rect(0, 0, self.bulset.width,
                                 self.bulset.height)
        self.rect2.centerx = ship.rect.centerx
        self.rect2.top = ship.rect.top

        self.speed_factor = self.bulset.a_speed_factor
        self.doublegun = self.bulset.doublegun

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y
        self.rect2.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def draw_bullets(self, bullets, idx= 0):
        for bullet in bullets.sprites():
            # bullet.doubler()
            # bullet.machinegun()
            bullet.draw_bullet()

    def doubler(self):
        self.rect.centerx = self.center + self.doublegun
        self.rect2.centerx = self.center - self.doublegun
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)

    def machinegun(self):
        self.speed_factor += 2

    def move_bullets(self, bullets, ship):
        new_bullet = Alien_bullet(self.bulset, self.screen, ship)
        bullets.add(new_bullet)

    def fire_bullets(self, bullets, aliens):
        for alien in aliens:
            self.move_bullets(bullets, alien)

    def draw_b(self, aliens, bullets):
        for alien in aliens:
            self.draw_bullets(bullets)
    def rid_excess_bullets(self, bullets):
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    def update_the_catridge(self, bullets):
        bullets.update()
        self.rid_excess_bullets(bullets)
    def fire_off(self, aliens, alien_bullets):
        for alien in aliens:
            self.update_the_catridge(alien_bullets)


