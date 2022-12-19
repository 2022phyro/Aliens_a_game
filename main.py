from game_func import *
from pygame.sprite import Group
from Alien_combo import ALIEN, GameStats
from Button import Button, Score


def run_game():
    # Initializing game
    pygame.init()
    base_screen = Screen_settings()
    bul_set = Bullet_settings()
    screen = pygame.display.set_mode((base_screen.screen_width, base_screen.screen_height))
    pygame.display.set_caption("ALIENS ATTACK")
    background = Background(screen)
    starship = Spaceship(screen, base_screen)
    bullet = Bullet(bul_set, screen, starship)
    play_button = Button(base_screen, screen, "PLAY")
    bullets = Group()
    alien = Alien(screen, base_screen)
    aliens = Group()
    alien_bullet = Alien_bullet(bul_set, screen, alien)
    alien_bullets = Group()
    stats = GameStats(base_screen)
    AL = ALIEN(stats, alien_bullet, alien)
    score = Score(base_screen, screen, stats)


#   The main loop for the game
    AL.create_fleet(base_screen, screen, aliens, alien_bullets)
    while True:

        check_events(starship, bullets, bullet, alien_bullet, alien_bullets, aliens, AL, play_button, base_screen, screen, bul_set, stats, score)
        if AL.stats.game_active:
            starship.update_ship_movements()
            AL.update_the_bullets(starship, base_screen, bullets, bullet, aliens, alien_bullets, screen,  stats, score)
            update_alien(base_screen, aliens, screen)
            alien_bullet.fire_off(aliens, alien_bullets)

    #       display the last screen
        draw_screen(background, starship, screen, bullets, aliens, alien_bullet, alien_bullets, AL, play_button, bullet.doubles, stats, score)

run_game()
