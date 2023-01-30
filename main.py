import pygame
import random
import os


WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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

rice_tray_rect = None
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


    #2 Update
    # all_sprites.update()


    #3 Draw/render
    # screen.fill(BLACK)
    screen.blit( wallpaper, (0, 0),)
    screen.blit( bench, (0, 0),)
    screen.blit( workstation, (0, 0),)
    rice_tray_rect = screen.blit( rice_tray, (75, 363),)
    screen.blit( mat, (0, 0),)
    screen.blit( rice_ball, (0, 0),)

    

    # all_sprites.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()