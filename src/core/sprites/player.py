import pygame
from sprites.projectile import Projectile
from animations.animation import AnimateSprite


class Player(AnimateSprite):
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.surface = self.game.surface
        self.health = 150
        self.name = "Player"
        self.max_health=150
        self.attack = 5
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 355

    def damage(self, sprite):
        if self.health<=0:
            self.game.game_over()
        else:
            self.health -= sprite.attack

    def update_animation(self):
        self.animate()

    def update_health_bar(self):
        back_bar_color = (60, 63, 60)
        front_bar_color = (111, 210, 46)

        height = 7
        border_radius = 10

        bar_position_x, bar_position_y = self.rect.x+38, self.rect.y+18

        back_bar_rect = (bar_position_x, bar_position_y, self.max_health, height)
        front_bar_rect = (bar_position_x, bar_position_y, self.health, height)

        pygame.draw.rect(self.surface, back_bar_color, back_bar_rect, border_radius=border_radius)
        pygame.draw.rect(self.surface, front_bar_color, front_bar_rect, border_radius=border_radius)    

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def launch_projectile(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        self.game.sound_manager.play("tir")
        self.start_animation()
