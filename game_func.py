import sys
import pygame.mouse
from bullets import *
from Drawing import *
def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += alien.gme.fleet_drop_speed
        alien.gme.fleet_direction *= -1
def check_fleet_edges(game_settings, aliens, screen):
    for alien in aliens.sprites():
        if alien.check_edges(screen):
            change_fleet_direction(game_settings, aliens)
            break

def update_alien(game_settings, aliens, screen):
    check_fleet_edges(game_settings, aliens, screen)
    aliens.update()
def start_game(AL, game_set, screen, aliens, alien_bullets, ship, bullets, bullet, bul_set, stats, score):
    AL.stats.game_active = True
    AL.stats.ship_remains = 5
    aliens.empty()
    alien_bullets.empty()
    bullets.empty()
    AL.create_fleet(game_set, screen, aliens, alien_bullets)
    ship.centered()
    game_set.dynamic_settings()
    bul_set.dynamic_settings()
    score.stats.reset_stats()
    score.prep_score()
    bullet.doubles = 0
    pygame.mouse.set_visible(False)
def check_play_button(AL, play_button, mouse_x, mouse_y, game_set, bullet, bul_set, stats, score,
                      screen, aliens, alien_bullets, bullets, ship):
    c =  play_button.rect.collidepoint(mouse_x, mouse_y)
    if c and not AL.stats.game_active:
        start_game(AL, game_set, screen, aliens, alien_bullets, ship, bullets, bullet, bul_set, stats, score)

def check_key_down(event, ship, bullet, bullets, alien_bullet, game_set, screen, bul_set, stats, score,
                   alien_bullets, aliens, AL, play_button):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not AL.stats.game_active:
            start_game(AL, game_set, screen, aliens, alien_bullets, ship, bullets, bullet, bul_set, stats, score)
        ship.move_ship(event)
        bullet.move_bullets(event, bullets)
        alien_bullet.fire_bullets(alien_bullets, aliens)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        check_play_button(AL, play_button, mouse_x, mouse_y, game_set, bullet, bul_set, stats, score,screen, aliens, alien_bullets, bullets, ship)

def check_events(ship, bullets, bullet, alien_bullet, alien_bullets, aliens, AL, play_button, game_set, screen, bul_set, stats, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down(event, ship, bullet, bullets, alien_bullet, game_set, screen, bul_set, stats, score, alien_bullets, aliens, AL, play_button)
        ship.stop_ship(event)



def draw_screen(background, ship, screen, bullets, aliens, alien_bullet, alien_bullets, AL, play_button, idx, stats, score):
    background.draw_background()
    ship.draw_ship()
    Bullet.draw_bullets(bullets, bullets, idx)
    aliens.draw(screen)
    alien_bullet.draw_b(aliens, alien_bullets)
    score.display_score()
    score.display_high_score()
    if not AL.stats.game_active:
        play_button.draw()

    pygame.display.flip()
