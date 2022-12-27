import pygame
from pygame.sprite import Sprite
"""The three functions below are functions or qualities shared by both alien and starship bullets
For that sole reason thy were set outside the classes"""


def powerup(bullet, ship, stats):
    if stats.level == 2:
        ship.speedup()
    elif stats.level == 3:
        bullet.doubler()
    elif stats.level == 4:
        bullet.machinegun()
    elif stats.level == 5:
        bullet.doubler()
        bullet.machinegun()
    elif stats.level == 6:
        bullet.machinegun()
    elif stats.level >= 7:
        ship.speedup()
        bullet.doubler()
        bullet.machinegun()


def draw_bullets(bullets, ship=None, stats=None):
    """This draws the bullets onto the screen"""
    for bullet in bullets.sprites():
        if ship:
            powerup(bullet, ship, ship.stats)
        elif stats:
            if stats.level == 4:
                bullet.doubler()
            elif stats.level == 5:
                bullet.machinegun()
            elif stats.level >= 6:
                bullet.doubler()
                bullet.machinegun()
        bullet.draw_bullet()


def rid_excess_bullets(bullets):
    """This removes the bullets that has passed off the screen"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_the_catridge(bullets):
    """This creates new bullets and remove old ones"""
    bullets.update()
    rid_excess_bullets(bullets)


class Bullet(Sprite):
    """This class contain all about bullets, as well as their powerups and their ranges"""
    def __init__(self, game_settings, screen, ship, stats):
        super(Bullet, self).__init__()
        self.screen = screen
        self.doubles = 0
        self.ship = ship
        self.gme = game_settings
        self.stats = stats
        self.rect = pygame.Rect(0, 0, self.gme.bullet_width,
                                self.gme.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.center = self.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = self.gme.bullet_color
        self.rect2 = pygame.Rect(0, 0, self.gme.bullet_width,
                                 self.gme.bullet_height)
        self.rect2.centerx = ship.rect.centerx
        self.rect2.top = ship.rect.top
       
        self.speed_factor = self.gme.bullet_speed_factor
        self.double_gun = self.gme.bullet_double_gun

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.rect2.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def doubler(self):
        self.rect.centerx = self.center + self.double_gun
        self.rect2.centerx = self.center - self.double_gun
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)

    def machinegun(self):
        self.speed_factor += 2

    def move_bullets(self, event, bullets):
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(self.gme, self.screen, self.ship, self.stats)
            bullets.add(new_bullet)


class AlienBullet(Sprite):
    def __init__(self, game_settings, screen, ship):
        super(AlienBullet, self).__init__()
        self.screen = screen
        self.ship = ship
        self.gme = game_settings
        self.rect = pygame.Rect(0, 0, self.gme.a_bullet_width,
                                self.gme.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.center = self.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = (0, 255, 255)
        self.rect2 = pygame.Rect(0, 0, self.gme.a_bullet_width,
                                 self.gme.bullet_height)
        self.rect2.centerx = ship.rect.centerx
        self.rect2.top = ship.rect.top

        self.speed_factor = self.gme.a_speed_factor
        self.double_gun = self.gme.bullet_double_gun

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y
        self.rect2.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def doubler(self):
        self.rect.centerx = self.center + self.double_gun
        self.rect2.centerx = self.center - self.double_gun
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)

    def machinegun(self):
        self.gme.a_bullet_width = 15
    def move_bullets(self, bullets, ship):
        new_bullet = AlienBullet(self.gme, self.screen, ship)
        bullets.add(new_bullet)

    def fire_bullets(self, bullets, aliens):
        for alien in aliens:
            self.move_bullets(bullets, alien)

    def draw_b(self, aliens, bullets, stats):
        for i in range(len(aliens)):
            draw_bullets(bullets, None, stats)

    def fire_off(self, aliens, alien_bullets):
        for alien in range(len(aliens)):
            update_the_catridge(alien_bullets)
