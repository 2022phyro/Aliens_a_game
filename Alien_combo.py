import pygame.sprite
from time import sleep
from bullets import *
from Drawing import *
from random import randint


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update(alien_bullet, alien_bullets, alien_ship):
    alien_ship.update()
    alien_bullet.update_the_catridge(alien_bullets)


def draw_alien(alien_ship, alien_bullet, alien_bullets):
    alien_ship.draw_alien()
    alien_bullet.draw_bullets(alien_bullets)


def create_fleet(game_settings, screen, aliens, alien_bullets):
    for i in range(2):
        for alien_no in range(game_settings.a_no_of_columns):
            n_a = Alien(game_settings, screen)
            n_a.width = n_a.rect.width
            n_a.x = n_a.width + randint(1, 2) * n_a.width * alien_no
            n_a.rect.x = n_a.x
            n_a.rect.y = n_a.rect.height + n_a.rect.height * i
            update_the_catridge(alien_bullets)

            aliens.add(n_a)


def collision_course(screen, starship, bullets, aliens, alien_bullets, game_settings, stats, sb):
    screen_rect = screen.get_rect()
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions.values():
            stats.score += game_settings.score_sc
            sb.prep_score()
        check_high_score(stats, sb)
    collision = pygame.sprite.groupcollide(bullets, alien_bullets, True, True)
    if collision:
        stats.ship_remains += 1
    if pygame.sprite.spritecollideany(starship, aliens):
        return True
    elif pygame.sprite.spritecollideany(starship, alien_bullets):
        return True
    else:
        for alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                return True


def update_the_bullets(starship, game_settings, bullets, bullet, aliens,
                       alien_bullets, screen, stats, sb, alien_ship, alien_bullet):
    update_the_catridge(aliens)
    a = collision_course(screen, starship, bullets, aliens, alien_bullets, game_settings, stats, sb)
    if a:
        ship_hit(starship, bullets, game_settings, screen, aliens, alien_bullets, sb, stats)
    if len(aliens) == 1 or len(aliens) == 0:
        bullets.empty()
        stats.level += 1
        sb.prep_level()
        create_fleet(game_settings, screen, aliens, alien_bullets)
        alien_ship.game_settings.speedup()
        alien_bullet.gme.speedup()
        bullet.doubles = 1


def ship_hit(ship, bullets, game_settings, screen, aliens, alien_bullets, sb, stats):
    if stats.ship_remains > 0:
        stats.ship_remains -= 1
        aliens.empty()
        alien_bullets.empty()
        bullets.empty()
        create_fleet(game_settings, screen, aliens, alien_bullets)
        ship.centered()
        sb.prep_ships()
    else:
        stats.game_active = False
        sb.record_high_score()
        pygame.mouse.set_visible(True)
#        pause the game for some time
    sleep(0.5)
