import sys
from bullets import *
from Drawing import *
from Alien_combo import ALIEN as A

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

def check_key_down(event, ship, bullet, bullets, alien_bullet, alien_bullets, aliens):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()
        ship.move_ship(event)
        bullet.move_bullets(event, bullets)
        alien_bullet.fire_bullets(alien_bullets, aliens)

def check_events(ship, bullets, bullet, alien_bullet, alien_bullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down(event, ship, bullet, bullets, alien_bullet, alien_bullets, aliens)
        ship.stop_ship(event)



def draw_screen(background, ship, screen, bullets, aliens, alien_bullet, alien_bullets):
    background.draw_background()
    ship.draw_ship()
    Bullet.draw_bullets(bullets, bullets)
    aliens.draw(screen)
    alien_bullet.draw_b(aliens, alien_bullets)

    pygame.display.flip()
