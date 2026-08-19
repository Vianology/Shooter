import pygame
from sprites.comet import Comet 

class CometFallEvent:
    def __init__(self, game):
        self.game = game
        self.surface = self.game.surface
        self.percent = 0
        self.percent_speed = 5
        self.fall_mode = False
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed/100

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >=100

    def meteor_fall(self):
        for comet in range(1, 6):
            self.all_comets.add(Comet(self, self.surface))

    def attemp_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters)==0:
            self.meteor_fall()
            self.fall_mode = True


    def update_bar(self):
        self.add_percent()
        back_bar_color = (0, 0, 0)
        front_bar_color = (187, 11, 11)

        height = 10
        border_radius = 10

        bar_position_x, bar_position_y = 0, self.surface.get_height()-height

        back_bar_rect = (bar_position_x, bar_position_y, self.surface.get_width(), height)
        front_bar_rect = (bar_position_x, bar_position_y, (self.surface.get_width()/100)*self.percent, height)

        pygame.draw.rect(self.surface, back_bar_color, back_bar_rect)
        pygame.draw.rect(self.surface, front_bar_color, front_bar_rect, border_radius=border_radius)

