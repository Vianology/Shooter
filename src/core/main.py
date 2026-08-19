import pygame
from sprites.game import Game

SCREEN_WIDTH = 1090
SCREEN_HEIGHT = 600

pygame.init()

clock = pygame.time.Clock()
FPS = 95

pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/images/ui/bg.jpg")

banner = pygame.image.load("assets/images/ui/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.centerx = screen.get_width()/2
banner_rect.bottom = screen.get_height()/2+200

play_button = pygame.image.load("assets/images/ui/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.centerx = screen.get_width()/2
play_button_rect.top = screen.get_height()/2+100

game = Game(screen)
running = True
while running:
    screen.blit(background, (0,-350))

    if game.is_playing:
        game.update()
    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button , play_button_rect)


    pygame.display.flip()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           print("Fermeture du jeu.")
           running = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    game.start()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False 
        elif event.type == pygame.MOUSEBUTTONDOWN and not game.is_playing:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play("click")
    clock.tick(FPS)

        



pygame.quit()
            
