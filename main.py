from game_func import *
from pygame.sprite import Group


def run_game():
#      Initializing game
    pygame.init()
    base_screen = Screen_settings()
    bul_set = Bullet_settings()
    screen = pygame.display.set_mode((base_screen.screen_width, base_screen.screen_height))
    pygame.display.set_caption("ALIENS ATTACK")
    background = Background(screen)
    starship = Spaceship(screen, base_screen)
    bullet = Bullet(bul_set, screen, starship)
    bullets = Group()
    alien = Alien(screen, base_screen)
    aliens = Group()
    alien.create_fleet(aliens)
    alien_bullets = Group()

#   The main loop for the game

    while True:
        check_events(starship, bullets, bullet)
        starship.update_ship_movements()
        bullet.update_the_catridge(bullets)
        alien.update_the_fleet(aliens)
#       display the last screen
        draw_screen(background, starship, screen, bullets, aliens)


run_game()
