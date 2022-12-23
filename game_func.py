import sys
import pygame.mouse

from Alien_combo import *


def start_game(game_set, screen, aliens, alien_bullets,
               ship, bullets, bullet, stats, score):
    stats.game_active = True
    stats.ship_remains = 5
    aliens.empty()
    alien_bullets.empty()
    bullets.empty()
    create_fleet(game_set, screen, aliens, alien_bullets)
    ship.centered()
    game_set.dynamic_settings()
    score.retrieve_high_score()
    score.prep_high_score()
    score.stats.reset_stats()
    score.prep_score()
    score.prep_level()
    bullet.doubles = 0
    pygame.mouse.set_visible(False)


def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += alien.gme.fleet_drop_speed
        alien.gme.fleet_direction *= -1


def check_fleet_edges(aliens, screen):
    for alien in aliens.sprites():
        if alien.check_edges(screen):
            change_fleet_direction(aliens)

            break


def update_alien(aliens, screen):
    check_fleet_edges(aliens, screen)
    aliens.update()


def check_play_button(play_button, mouse_x, mouse_y, game_set, bullet, stats, score,
                      screen, aliens, alien_bullets, bullets, ship):
    c = play_button.rect.collidepoint(mouse_x, mouse_y)
    if c and not stats.game_active:
        start_game(game_set, screen, aliens, alien_bullets,
                   ship, bullets, bullet, stats, score)


def check_key_down(event, ship, bullet, bullets, alien_bullet, game_set, screen, stats, score,
                   alien_bullets, aliens, play_button):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not stats.game_active:
            start_game(game_set, screen, aliens, alien_bullets,
                       ship, bullets, bullet, stats, score)
        ship.move_ship(event)
        bullet.move_bullets(event, bullets)
        alien_bullet.fire_bullets(alien_bullets, aliens)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        check_play_button(play_button, mouse_x, mouse_y, game_set, bullet, stats, score,
                          screen, aliens, alien_bullets, bullets, ship)


def check_events(ship, bullets, bullet, alien_bullet, alien_bullets, aliens,
                 play_button, game_set, screen, stats, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down(event, ship, bullet, bullets, alien_bullet, game_set, screen,
                       stats, score, alien_bullets, aliens, play_button)
        ship.stop_ship(event)


def draw_screen(background, ship, screen, bullets, aliens, alien_bullet, alien_bullets, play_button, stats, score):
    background.draw_background()
    ship.draw_ship()
    draw_bullets(bullets, ship)
    aliens.draw(screen)
    alien_bullet.draw_b(aliens, alien_bullets, ship.stats)
    score.display_score()
    score.display_high_score()
    score.display_level()
    if not stats.game_active:
        play_button.draw()
    pygame.display.flip()
