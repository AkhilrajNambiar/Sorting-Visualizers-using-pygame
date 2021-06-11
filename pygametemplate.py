import pygame
import random

WIDTH = 1000
HEIGHT = 600
FPS = 30
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Initializing pygame and setting game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bubble Sort Visualizer')
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
running = True
# Game loop
while running:
    clock.tick(FPS)
    # event processing part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating part
    all_sprites.update()
    # rendering part
    screen.fill(blue)
    all_sprites.draw(screen)
    # after drawing everything we have to flip the screen
    pygame.display.flip()

pygame.quit()
