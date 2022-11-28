import pygame
from pygame.sprite import Sprite
from random import randint


class Screen_settings:
    def __init__(self):
        """Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 690
        self.factor = 2.5
        self.fleet_direction = 1
        self.fleet_drop_speed = 20


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
        self.movement_factor = 1
        self.image = pygame.image.load('Images/The_Alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x  = self.rect.width
        self.rect.y = self.rect.height
        self.gme = Screen_settings()

        self.x = float(self.rect.x)
        self.x = float(self.rect.y)
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.x += (self.movement_factor * self.gme.fleet_direction)
        self.rect.x = self.x
    def check_edges(self, screen):
        self.screen_rect = screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False


