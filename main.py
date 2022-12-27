from game_func import *
from pygame.sprite import Group
from Alien_combo import *
from Button import Button, Score, GameStats
from bullets import *


def run_game():
    # Initializing game
    pygame.init()
    base_screen = ScreenSettings()
    screen = pygame.display.set_mode((base_screen.screen_width, base_screen.screen_height))
    pygame.display.set_caption("ALIENS ATTACK")
    background = Background(screen)
    stats = GameStats(base_screen)
    starship = Spaceship(screen, base_screen, stats)
    bullet = Bullet(base_screen, screen, starship, stats)
    play_button = Button(screen, "PLAY")
    bullets = Group()
    alien = Alien(screen, base_screen)
    aliens = Group()
    alien_bullet = AlienBullet(base_screen, screen, alien)
    alien_bullets = Group()
    score = Score(base_screen, screen, stats)


#   The main loop for the game
#     AL.create_fleet(base_screen, screen, aliens, alien_bullets)
    while True:

        check_events(starship, bullets, bullet, alien_bullet, alien_bullets, aliens,
                     play_button, base_screen, screen, stats, score)
        if stats.game_active:
            starship.update_ship_movements()
            update_the_catridge(bullets)
            update_the_bullets(starship, base_screen, bullets, bullet, aliens,
                               alien_bullets, screen, stats, score, alien, alien_bullet)
            update_alien(aliens, screen)
            alien_bullet.fire_off(aliens, alien_bullets)

    #       display the last screen
        draw_screen(background, starship, screen, bullets, aliens,
                    alien_bullet, alien_bullets, play_button, stats, score)

if __name__ == '__main__':
    run_game()
