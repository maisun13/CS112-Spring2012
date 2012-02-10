#!/usr/bin/env python

#voodoo
import pygame
from pygame.locals import *

screen_size = 640, 480
background = 0,0,0

#init pygame
pygame.init()
screen = pygame.display.set_mode(screen_size)

done=False 
while not done:
    event = pygame.event.poll()

    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
    elif event.type == KEYDOWN and event.key == K_w:
        background=255,255,255
    elif event.type == MOUSEBUTTONDOWN:
        print "Mouse",pygame.mouse.get_pos()

    screen.fill(background)
    pygame.display.flip()

print "Bye bye :D"
