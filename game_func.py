import sys
from bullets import *
from Drawing import *


def check_key_down(event, ship, bullet, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()
        ship.move_ship(event)
        bullet.move_bullets(event, bullets)


def check_events(ship, bullets, bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down(event, ship, bullet, bullets)
        ship.stop_ship(event) 


def draw_screen(background, ship, screen, bullets, aliens):
    background.draw_background()
    aliens.draw(screen)
    ship.draw_ship()
    Bullet.draw_bullets(bullets, bullets)
    pygame.display.flip()
