import pygame.font
class Button():
    def __init__(self, game_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont("Harrington", 48, "bold", "italic")
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
class Score():
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (45, 250, 15)
        self.font = pygame.font.SysFont("Old English Text", 32, "italic")
        self.prep_high_score()
        self.prep_score()
    def prep_score(self):
        figure = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(figure, True, self.text_color,
                                          (3, 4, 8))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = self.screen_rect.top + 15
        self.score_rect.right = self.screen_rect.right - 20
    def display_score(self):
        self.screen.blit(self.score_image, self.score_rect)
    def prep_high_score(self):
        high_score = "{:,}".format(self.stats.high_score)
        self.high_score = self.font.render(high_score, True, self.text_color,
                                            (3, 4, 8))
        self.high_rect = self.high_score.get_rect()
        self.high_rect.top = self.screen_rect.top + 15
        self.high_rect.centerx = self.screen_rect.centerx - 20
    def display_high_score(self):
        self.screen.blit(self.high_score, self.high_rect)


