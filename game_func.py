import sys
from Drawing import *


def move_ship_keydown(event, ship):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.right = True
        if event.key == pygame.K_LEFT:
            ship.left = True
        if event.key == pygame.K_UP:
            ship.up = True
        if event.key == pygame.K_DOWN:
            ship.down = True

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


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        move_ship_keydown(event,ship)
        stop_ship_keyup(event, ship)

def draw_screen(background, ship, screen):
    background.draw_background()
    ship.draw_ship()
    pygame.display.flip()


