import pygame
from pygame.sprite import Sprite


class ScreenSettings:
    def __init__(self):
        """Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 690
        self.factor = 2.5
        self.s_scale = 1.1
        self.score_scale = 5
        self.high_score = 0
        """Alien_fleet settings"""
        self.a_no_of_columns = int(4)
        """All the necessary bullet settings"""
        self.bullet_width = 1.5
        self.a_bullet_width = 1.5
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullet_double_gun = 25
        self.bullet_s_scale = 1.1
        self.bullet_speed_factor = 3.5
        self.dynamic_settings()
    
    def dynamic_settings(self):
        self.fleet_direction = 1
        self.fleet_drop_speed = 15
        self.ship_limit = 4
        self.movement_factor = 1.1
        self.score_sc = 5
        self.a_speed_factor = 0.5
    
    def speedup(self):
        self.fleet_drop_speed *= self.s_scale
        self.movement_factor *= self.s_scale
        self.fleet_direction *= self.s_scale
        self.score_sc += self.score_scale
        self.a_speed_factor *= self.bullet_s_scale

    def returns(self):
        self.fleet_direction = 1
        self.fleet_drop_speed = 20
        self.movement_factor = 2


class Background:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/The_background.bmp').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    def draw_background(self):
        """Draw the background"""
        self.screen.blit(self.image, self.rect)


class Spaceship:
    def __init__(self, screen, game_settings, stats):
        """Movement flags"""
        self.right = False
        self.left = False
        self.stats = stats
        self.up = False
        self.down = False
        self.game_settings = game_settings
        self.screen = screen
        self.image = pygame.image.load('Images/The_starship.bmp')
        self.image.set_colorkey((3, 4, 8))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def draw_ship(self):
        """Draw the starship"""
        self.screen.blit(self.image, self.rect)

    def centered(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom

    def speedup(self):
        self.game_settings.factor = 4

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
        self.image.set_colorkey((3, 4, 8))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.gme = ScreenSettings()

        self.x = float(self.rect.x)
        self.x = float(self.rect.y)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        self.x += (self.gme.movement_factor * self.gme.fleet_direction)
        self.rect.x = self.x

    def check_edges(self, screen):
        self.screen_rect = screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
