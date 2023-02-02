import pygame
import random
import os


WIDTH = 360
HEIGHT = 480
PADDING = 5
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Useful constants
OFFSETS = [(-PADDING*2, -PADDING*2), (PADDING*2, -PADDING*2), (-PADDING*2, PADDING*2), (PADDING*2, PADDING*2)]

## initialize pygame and create window
pygame.init()
# pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS

wallpaper = pygame.image.load('assets/wallpaper.png').convert()
bench = pygame.image.load('assets/bench.png').convert_alpha()
workstation = pygame.image.load('assets/workstation.png').convert_alpha()
rice_tray = pygame.image.load('assets/rice_tray.png').convert_alpha()
mat = pygame.image.load('assets/mat.png').convert_alpha()
rice_ball = pygame.image.load('assets/rice_ball.png').convert_alpha()
seaweed_tray = pygame.image.load('assets/seaweed_tray.png').convert_alpha()
seaweed = pygame.image.load('assets/seaweed.png').convert_alpha()

rice_tray_rect = None
seaweed_tray_rect = None
mat_rect = None
seaweed_placed = False
ingredients = []
# print(files)
## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if rice_tray_rect.collidepoint(pos):
                print("Rice Tray")
                if len(ingredients) < 4:
                    ingredients.append(rice_ball)
            if seaweed_tray_rect.collidepoint(pos):
                print("Seaweed Tray")
                seaweed_placed = True
                print(seaweed_placed)
            if mat_rect.collidepoint(pos):
                ingredients = []
                seaweed_placed = False

    #2 Update
    # all_sprites.update()


    #3 Draw/render
    # screen.fill(BLACK)
    work_station_height = HEIGHT-workstation.get_height()
    bench_height = HEIGHT-bench.get_height()
    screen.blit( wallpaper, (0, 0),)
    screen.blit( bench, (0, bench_height),)
    screen.blit( workstation, (PADDING, work_station_height),)
    rice_tray_rect = screen.blit( rice_tray, (PADDING*4 + mat.get_width(), work_station_height+PADDING*2),)
    seaweed_tray_rect = screen.blit( seaweed_tray, (PADDING*5 + mat.get_width() + rice_tray.get_width(), work_station_height+PADDING*2))
    mat_rect = screen.blit( mat, (PADDING*3, work_station_height+PADDING*2),)
    if seaweed_placed:
        # print("blitting")
        screen.blit( seaweed, (PADDING*4, work_station_height+PADDING*3),)
    # screen.blit( seaweed, (PADDING*4, work_station_height+PADDING*3))
    # screen.blit( seaweed, (0, 0))
    seaweed_height = work_station_height+PADDING*3
    seaweed_width = PADDING*4
    for i, ing in enumerate(ingredients):
        screen.blit( ing, (seaweed_width + seaweed.get_width()/2 + OFFSETS[i][0] - ing.get_width()/2, seaweed_height + seaweed.get_height()/2 + OFFSETS[i][1] - ing.get_height()/2))
    screen.blit( rice_ball, (0, 0),)

    

    # all_sprites.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()