import pygame
from pygame.sprite import Sprite
from random import randint



class Screen_settings:
    def __init__(self):
        """Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 690
        self.factor = 2.5


class Background:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/The_background.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    def draw_background(self):
    #Draw the baackground
        self.screen.blit(self.image, self.rect)

class Spaceship:
    def __init__(self, screen, game_settings):
        #Movement flags
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.game_settings = game_settings
        self.screen = screen
        self.image = pygame.image.load('Images/The_starship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)


    def draw_ship(self):
    #Draw the starship
        self.screen.blit(self.image, self.rect)

    def move_ship(self, event):
        if event.key == pygame.K_RIGHT:
            self.right = True
        if event.key == pygame.K_LEFT:
            self.left = True
        if event.key == pygame.K_UP:
            self.up = True
        if event.key == pygame.K_DOWN:
           self.down = True

    def stop_ship(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_UP:
                self.up = False
            if event.key == pygame.K_DOWN:
                self.down = False
    def update_ship_movements(self):
        if self.right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.factor
        if self.left and self.rect.left > 0:
            self.center -= self.game_settings.factor
        self.rect.centerx = self.center
        if self.up and self.rect.top > self.screen_rect.top:
                self.bottom -= self.game_settings.factor
        if self.down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.game_settings.factor
        self.rect.bottom = self.bottom

class Alien(Sprite):
    def __init__(self, screen, game_settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load('Images/The_Alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx -= 50

        self.rect.x  = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.x = float(self.rect.y)
        self.fleet_speed = self.game_settings.factor
        self.fleet_direction = 1
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.x += self.game_settings.factor - 2
        self.rect.x = self.x
    def rid_excess_fleet(self, aliens):
        for bullet in aliens.copy():
            if bullet.rect.bottom <= 0:
               aliens.remove(bullet)
    def update_the_fleet(self, aliens):
        self.check_fleet_edges(aliens)
        aliens.update()
        self.rid_excess_fleet(aliens)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return False
        self.x += (self.game_settings.factor * self.fleet_direction)
    def check_fleet_edges(self, aliens):
        for alien in aliens.sprites():
            if alien.check_edges():
                alien.change_fleet(aliens)
                break

    def change_fleet(self, aliens):
        for alien in aliens.sprites():
            alien.rect.y += alien.game_settings.factor - 1.5
            alien.fleet_direction *= -1

    def create_fleet(self, aliens):
        no_of_aliens = int(5)
        for alien_serial in range(no_of_aliens):
            new_alien = Alien(self.screen, self.game_settings)
            new_alien.x = self.rect.width + randint(2,2) * self.rect.width * alien_serial
            new_alien.rect.x = new_alien.x
            aliens.add(new_alien)