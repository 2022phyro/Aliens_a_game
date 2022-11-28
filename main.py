from game_func import *
from pygame.sprite import Group
from Alien_combo import *


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
    alien_bullet = Alien_bullet(bul_set, screen, alien)
    alien_bullets = Group()
    AL = ALIEN(alien_bullet, alien)

#   The main loop for the game
    AL.create_fleet(base_screen, screen, aliens, alien_bullets)
    while True:
        check_events(starship, bullets, bullet, alien_bullet, alien_bullets, aliens)
        starship.update_ship_movements()
        bullet.update_the_catridge(bullets)
        alien_bullet.fire_off(aliens, alien_bullets)

#       display the last screen
        draw_screen(background, starship, screen, bullets, aliens, alien_bullet, alien_bullets)


run_game()
