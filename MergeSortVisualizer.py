import pygame
import random
import sys
import time


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
pygame.display.set_caption('Merge Sort Visualizer')
clock = pygame.time.Clock()
array = [random.randint(1,500) for i in range(32)]
r = len(array) - 1
p = 0

swoosh = pygame.mixer.Sound('swoosh.mp3')

running = True

class Bars(pygame.sprite.Sprite):
    def __init__(self, height, left):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, height))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        self.rect.left = left
        self.speed = 5

def draw_text(surface, text, pos, size):
    font_name = pygame.font.match_font('calibri')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect()
    text_rect.topleft = pos
    surface.blit(text_surface, text_rect)

def merge(A,p,q,m,r):
    n1 = q-p+1
    n2 = r-m+1
    # Creating two arrays left(L) and Right(R)
    L = []
    R = []
    # Copy the elements A[p...q] to L
    for i in range(p,q+1):
        L.append(A[i])
    # Copy the elements A[m...r] to R
    for j in range(m,r+1):
        R.append(A[j])
    # Add a sentinel value to check if either left or right array
    # has become empty
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = 0
    j = 0
    k = p
    while k <= r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            k += 1
            swoosh.play()
        else:
            A[k] = R[j]
            j += 1
            k += 1
            print(R[j])
            swoosh.play()
        all_sprites = pygame.sprite.Group()
        bars = []
        first_left = 5
        for bar_height in array:
            bars.append(Bars(bar_height, first_left))
            first_left += 30
        try:
            if k <= q:
                key = bars[k]
                key.image.fill(green)
            elif k > m:
                key = bars[k]
                key.image.fill(red)
        except IndexError as e:
            print("Index ke bahar jaata hai kabhi kabhi")
        for bar in bars:
            all_sprites.add(bar)
        time.sleep(0.05)
        all_sprites.update()
        # rendering part
        screen.fill(blue)
        draw_text(screen,'Merge Sort Visualizer',(5,0),60)
        all_sprites.draw(screen)
        # after drawing everything we have to flip the screen
        pygame.display.flip()
    return A

def merge_sort(A,p,r):
    if p < r:
        mid = (p + r)//2
        merge_sort(A,p,mid)
        merge_sort(A,mid+1,r)
        return merge(A,p,mid,mid+1,r)


# Game loop
while running:
    clock.tick(FPS)
    # event processing part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating part
    merge_sort(array,0,r)
    running = False

pygame.quit()
