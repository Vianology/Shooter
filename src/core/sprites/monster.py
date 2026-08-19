import pygame
import random
from animations.animation import AnimateSprite

class Monster(AnimateSprite):
    def __init__(self, game, sprite_name, size, offset=0):
        super().__init__(sprite_name, size)
        self.game = game
        self.surface = self.game.surface
        # self.sprite_name = "Monster"
        self.health = 100
        self.max_health = 100
        self.attack = 0.01
        self.rect = self.image.get_rect()
        self.rect.x = 700+random.randint(0, 300)
        self.rect.y = 395-offset
        self.loot_amount = 10
        self.start_animation()

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            self.animation_state = True
        else:
            for player in self.game.check_collision(self, self.game.all_players):
                player.damage(self)
            self.animation_state = False

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self):
        back_bar_color = (60, 63, 60)
        front_bar_color = (111, 210, 46)

        height = 5
        border_radius = 10

        bar_position_x, bar_position_y = self.rect.x+38, self.rect.y-8

        back_bar_rect = (bar_position_x, bar_position_y, self.max_health, height)
        front_bar_rect = (bar_position_x, bar_position_y, self.health, height)

        pygame.draw.rect(self.surface, back_bar_color, back_bar_rect, border_radius=border_radius)
        pygame.draw.rect(self.surface, front_bar_color, front_bar_rect, border_radius=border_radius)

    def remove(self):
        self.game.all_monsters.remove(self)

    def set_loot_amount(self, amount):
        self.loot_amount = amount
        

    def set_speed(self, speed=2):
        self.default_speed = speed
        self.velocity = random.uniform(1, self.default_speed)


    def damage(self, sprite):
        if self.health<=0:
            self.rect.x = 700+random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.uniform(1, self.default_speed)
            self.game.add_score(self.loot_amount)
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attemp_fall()
        else:
            self.health -= sprite.attack

class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(2)
        self.set_loot_amount(20)

class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.2
        self.set_speed(1)
        self.set_loot_amount(30)