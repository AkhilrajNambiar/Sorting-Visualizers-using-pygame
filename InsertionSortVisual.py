import random
import time
import pygame

WIDTH = 1000
HEIGHT = 600
FPS = 30
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Initializing pygame and setting game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Insertion Sort Visualizer')
clock = pygame.time.Clock()
array = [random.randint(1,500) for i in range(32)]

class Bars(pygame.sprite.Sprite):
    def __init__(self, height, left):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, height))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.left = left
        self.speed = 5

def font_draw(surface, text, size, pos):
    font_name = pygame.font.match_font('calibri')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect()
    text_rect.topleft = pos
    surface.blit(text_surface, text_rect)

swoosh = pygame.mixer.Sound('swoosh.mp3')
running = True
# Game loop
while running:
    clock.tick(FPS)
    # event processing part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating part
    n = len(array)
    bars = []
    for j in range(1,n):
        key = array[j]
        i = j - 1
        not_over = False
        while i >= 0 and array[i] > key:
            not_over = True
            array[i+1] = array[i]
            swoosh.play()
            i = i - 1
            all_sprites = pygame.sprite.Group()
            bars = []
            first_left = 5
            for m in array:
                bars.append(Bars(m, first_left))
                first_left += 30
            key_color = bars[j]
            key_color.image.fill(green)
            comparer = bars[i]
            comparer.image.fill(red)
            for bar in bars:
                all_sprites.add(bar)
            time.sleep(0.05)
            all_sprites.update()
            # rendering part
            screen.fill(blue)
            font_draw(screen, 'Insertion Sort Visualization', 60, (0,0))
            all_sprites.draw(screen)
            # after drawing everything we have to flip the screen
            pygame.display.flip()
        array[i + 1] = key
        if not_over:
            swoosh.play()

pygame.quit()
