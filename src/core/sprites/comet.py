import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_fall_event, surface):
        super().__init__()
        self.comet_fall_event = comet_fall_event
        self.surface = surface
        self.image = pygame.image.load("assets/images/entities/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.uniform(1, 2.3)
        self.attack = 5
        self.rect.x = random.randint((self.image.get_width()), self.surface.get_width()-self.image.get_width())
        self.rect.y = -random.randint(0, self.image.get_height())


    def fall(self):
        self.rect.y += self.velocity

        if  self.rect.y >=self.surface.get_height():
            self.remove()
            if len(self.comet_fall_event.all_comets):
                self.comet_fall_event.reset_percent()
                self.comet_fall_event.fall_mode = False


        if self.comet_fall_event.game.check_collision(self, self.comet_fall_event.game.all_players):
            self.remove()
            for player in self.comet_fall_event.game.all_players:
                player.damage(self)

    def remove(self):
        self.kill()
        self.comet_fall_event.game.sound_manager.play("meteorite")
        if len(self.comet_fall_event.all_comets) ==0:
            self.comet_fall_event.reset_percent()
            self.comet_fall_event.game.start()

