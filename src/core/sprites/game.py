import pygame
from sprites.player import Player
from sprites.monster import Mummy
from sprites.monster import Alien
from events.comet_event import CometFallEvent
from events.sounds import SoundManager


class Game:
    def __init__(self, surface):
        self.is_playing = False
        self.surface = surface
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.font = pygame.font.Font("assets/fonts/SpaceMono-Bold.ttf", 25)
        self.sound_manager = SoundManager()
        


    def start(self):
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        self.is_playing = True

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play("game_over")

    def update(self):
        score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
        self.surface.blit(score_text, (20, 20))

        self.surface.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectiles:
            projectile.move(self.surface)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar()
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.update_health_bar() 
        self.player.update_animation()
        self.player.all_projectiles.draw(self.surface)
        self.all_monsters.draw(self.surface)
        self.comet_event.update_bar()
        self.comet_event.all_comets.draw(self.surface)

        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x>0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x+self.player.rect.width<self.surface.get_width():
            self.player.move_right()

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)