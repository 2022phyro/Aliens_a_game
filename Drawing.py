from all_imports import *

class Screen_settings:
    def __init__(self):
        """Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 690
        self.factor = 2.5


class Background:
    def __init__(self, screen):
        self.screen = screen
        
        self.image = pygame.image.load('The_background.bmp')
        self.image.set_colorkey((0, 0, 0))
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
        self.image = pygame.image.load('The_starship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)


    def draw_ship(self):
    #Draw the starship
        self.screen.blit(self.image, self.rect)
        
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


