 #!/usr/bin/env python

import pygame
from pygame import draw
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))

screen.fill((0,0,0))
done = False
def draw_tie(surf, color, pos):
    x, y = pos
    draw.rect(surf, color, (x,y,5,40))
    draw.rect(surf, color, (x+35,y,5,40))
    draw.rect(surf, color, (x,y+17,40,5))
    draw.circle(surf, color, (x+20,y+20), 10)

col = 200
dir = 1

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            draw_tie(screen, (col,0,col), pygame.mouse.get_pos())

    #draw tie fighter
    col += dir
    if col > 255 or col < 100:
        dir *= -1
        col += dir
   
    pygame.display.flip()


