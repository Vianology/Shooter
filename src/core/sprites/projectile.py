import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 6
        self.image = pygame.image.load("assets/images/entities/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.player_midright_x, self.player_midright_y = self.player.rect.midright
        self.rect.x = self.player_midright_x-70
        self.rect.y = self.player_midright_y
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        # self.rect.center = self.origin_image.get_rect().center

    # def remove(self):
    #     self.player.all_projectiles.remove(self)


    def move(self, screen):
        self.rect.x += self.velocity
        self.rotate()
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            monster.damage(self.player)
            self.kill()
            return
        if self.rect.x>screen.get_width():
            self.kill()