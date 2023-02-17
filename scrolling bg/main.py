import pygame 
import os
import math

pygame.init()

rocket1 = pygame.image.load(os.path.join('hampyship.png'))
rocket = pygame.transform.scale(rocket1, (100, 100))
CLOCK = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 367
playing = True
RED = (200, 150, 255)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('infinite scroll')
bg = pygame.image.load("bg loop.jpg")

bg_width = bg.get_width()
bg_height = bg.get_height()
bg_rect = bg.get_rect()
scroll = 0
x_pos = 20
y_pos = 20
step = 5
angle = 0
move_right = False
move_left = False
move_down = False
move_up = False
gravity = 0

tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
while playing:


    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity -=30

        



        
    for i in range(0, tiles ):
        window.blit(bg,(i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        scroll -= 5
        if abs(scroll) > bg_width:
            scroll = 0
    gravity += 3  
    window.blit(rocket1, (20, gravity))
    CLOCK.tick(FPS)
    pygame.display.update()
else:
    pygame.quit()

