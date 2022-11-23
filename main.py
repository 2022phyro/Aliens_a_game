from game_func import *

def rungame():
    #Initializing game
    pygame.init()
    base_screen = Screen_settings()
    screen = pygame.display.set_mode((base_screen.screen_width, base_screen.screen_height))
    pygame.display.set_caption("ALIENS ATTACK")


    background = Background(screen)
    starship = Spaceship(screen, base_screen)
    #The main loop for the game

    while True:
        check_events(starship)
        starship.update_ship_movements()
        #display the last screen
        draw_screen(background, starship, screen)



rungame()
