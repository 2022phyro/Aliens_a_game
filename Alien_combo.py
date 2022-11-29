import pygame.sprite

from Drawing import *

class ALIEN(Sprite):
    def __init__(self, alien_bullet, alien_ship):
        super(ALIEN, self).__init__()
        self.alien_bullet = alien_bullet
        self.alien_ship = alien_ship
        self.no_of_columns = int(3)

    def update(self, alien_bullets):
        self.alien_ship.update()
        self.alien_bullet.update_the_catridge(alien_bullets)

    def draw_alien(self, alien_bullets):
        self.alien_ship.draw_alien()
        self.alien_bullet.draw_bullets(alien_bullets)
        
    def move_bullet(self, alien_bullets, aliens):
        for alien in aliens:
            self.alien_bullet.move_bullets(alien_bullets)
       
    def create_fleet(self, game_settings, screen, aliens, alien_bullets):
        for alien_no in range(self.no_of_columns):
            n_a = Alien(game_settings, screen)
            n_a.width = n_a.rect.width
            n_a.x = n_a.width + randint(1, 2) * n_a.width * alien_no
            n_a.rect.x = n_a.x
            # n_a.rect.y = n_a.rect.height + randint(1, 2) * n_a.rect.height * row_number
            self.alien_bullet.update_the_catridge(alien_bullets)
            aliens.add(n_a)
    def collision_course(self, starship, bullets, aliens, alien_bullets):
        idx = 0
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        collision = pygame.sprite.groupcollide(bullets, alien_bullets, True, True)
        if pygame.sprite.spritecollideany(starship, aliens):
            print("Ship hit!")
        elif pygame.sprite.spritecollideany(starship, alien_bullets):
            print("SHIP HIT!!")
    def update_the_bullets(self, starship, game_settings, bullets, bullet, aliens, alien_bullets, screen):
        bullet.update_the_catridge(bullets, aliens)
        self.collision_course(starship, bullets, aliens, alien_bullets)
        if len(aliens) < 1:
            bullets.empty()
            self.create_fleet(game_settings, screen, aliens, alien_bullets)


class GameStats():
    def __init__(self, game_settings):
        self.gme = game_settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_remains = self.game_settings.ship_limit
