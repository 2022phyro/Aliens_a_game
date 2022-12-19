import pygame.sprite
from time import sleep
from Drawing import *
def check_high_score(stats, sb):
  if stats.score > stats.high_score:
      stats.high_score = stats.score
      sb.prep_high_score()

class ALIEN(Sprite):
    def __init__(self, gme_sts, alien_bullet, alien_ship):
        super(ALIEN, self).__init__()
        self.alien_bullet = alien_bullet
        self.alien_ship = alien_ship
        self.no_of_columns = int(4)
        self.stats = gme_sts
        # self.stats.game_active = False

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
        for i in range(2):
            for alien_no in range(self.no_of_columns):
                n_a = Alien(game_settings, screen)
                n_a.width = n_a.rect.width
                n_a.x = n_a.width + randint(1, 2) * n_a.width * alien_no
                n_a.rect.x = n_a.x
                n_a.rect.y = n_a.rect.height + n_a.rect.height * i
                self.alien_bullet.update_the_catridge(alien_bullets)
                aliens.add(n_a)
    def collision_course(self, screen, starship, bullets, aliens, alien_bullets, game_settings, stats, sb):
        screen_rect = screen.get_rect()
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
            for alien in collisions.values():
                stats.score += game_settings.score_sc
                sb.prep_score()
            check_high_score(stats, sb)
        collision = pygame.sprite.groupcollide(bullets, alien_bullets, True, True)
        if pygame.sprite.spritecollideany(starship, aliens):
            return True
        elif pygame.sprite.spritecollideany(starship, alien_bullets):
            return True
        else:
            for alien in aliens.sprites():
                if alien.rect.bottom >= screen_rect.bottom:
                    return True
    def update_the_bullets(self, starship, game_settings, bullets, bullet, aliens, alien_bullets, screen,stats, sb):
        bullet.update_the_catridge(bullets, aliens)
        a = self.collision_course(screen, starship, bullets, aliens, alien_bullets, game_settings, stats, sb)
        if (a):
            self.ship_hit(starship, bullets, game_settings, screen, aliens, alien_bullets, bullet)
        if len(aliens) == 1:
            bullets.empty()
            self.create_fleet(game_settings, screen, aliens, alien_bullets)
            self.alien_ship.game_settings.speedup()
            self.alien_bullet.bulset.speedup()
            bullet.doubles = 1
    def ship_hit(self, ship, bullets, game_settings, screen, aliens, alien_bullets, bullet):
        if self.stats.ship_remains > 0:
            self.stats.ship_remains -= 1
            aliens.empty()
            alien_bullets.empty()
            bullets.empty()
            self.create_fleet(game_settings, screen, aliens, alien_bullets)
            ship.centered()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        #pause the game for some time
        sleep(0.5)



class GameStats():
    def __init__(self, game_settings):
        self.gme = game_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ship_remains = self.gme.ship_limit
        self.score = 0
