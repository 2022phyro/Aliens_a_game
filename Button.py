import pygame.font
import json
from pygame.sprite import Group, Sprite


class GameStats:
    def __init__(self, game_settings):
        self.gme = game_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ship_remains = self.gme.ship_limit
        self.score = 0
        self.level = 1


class Life(Sprite):
    def __init__(self, screen):
        super(Life, self).__init__()
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("Images/Lifeline.jpg")
        self.image.set_colorkey((3, 4, 8))
        self.rect = self.image.get_rect()
        self.rect.top = self.screen_rect.top + 15
        self.rect.left = self.screen_rect.left + 20
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


class Button:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 255)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont("Chiller", 48, "bold", "italic")
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Score:
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (156,  200, 15)
        self.back = (3, 4, 8)
        self.font = pygame.font.SysFont("Old English Text", 28, "italic")
        self.prep_high_score()
        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        figure = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(figure, True, self.text_color,
                                            self.back)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = self.screen_rect.top + 15
        self.score_rect.right = self.screen_rect.right - 20

    def display_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        high_score = "{:,}".format(self.stats.high_score)
        self.high_score = self.font.render(high_score, True, self.text_color,
                                           self.back)
        self.high_rect = self.high_score.get_rect()
        self.high_rect.top = self.screen_rect.top + 15
        self.high_rect.centerx = self.screen_rect.centerx - 20

    def prep_ships(self):
        self.ships = Group()
        for num in range(self.stats.ship_remains):
            ship = Life(self.screen)
            ship .rect.x = 10 + num * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def display_high_score(self):
        self.screen.blit(self.high_score, self.high_rect)

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.back)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.screen_rect.top + 45

    def display_level(self):
        self.screen.blit(self.level_image, self.level_rect)

    def record_high_score(self):
        with open("record.json", 'w') as f:
            json.dump(str(self.stats.high_score), f)

    def retrieve_high_score(self):
        with open("record.json", 'r') as f:
            self.stats.high_score = int(json.load(f))
