
import sys
from Bulets import *
from Drawing import *


def move_ship_keydown(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.right = True
    if event.key == pygame.K_LEFT:
        ship.left = True
    if event.key == pygame.K_UP:
        ship.up = True
    if event.key == pygame.K_DOWN:
       ship.down = True
def move_bullets(event, bullets, bullet_settings, screen, ship):
    if event.key == pygame.K_SPACE and len(bullets) < 3:
        new_bullet = Bullet(bullet_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown(event,ship, bullets, bullet_settings, screen):
     if event.type == pygame.KEYDOWN:
         move_ship_keydown(event, ship)
         move_bullets(event, bullets, bullet_settings, screen, ship)

def stop_ship_keyup(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.right = False
        if event.key == pygame.K_LEFT:
            ship.left = False
        if event.key == pygame.K_UP:
            ship.up = False
        if event.key == pygame.K_DOWN:
            ship.down = False
def rid_excess_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def update_the_bullets(bullets):
    bullets.update()
    rid_excess_bullets(bullets)

def check_events(ship, bullets, bullet_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_keydown(event,ship, bullets, bullet_settings, screen)
        stop_ship_keyup(event, ship)

def draw_screen(background, ship, screen, bullets):
    background.draw_background()
    ship.draw_ship()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


