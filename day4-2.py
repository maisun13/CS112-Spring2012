#!/usr/bin/env python

import pygame

screen_size = 640, 480
background = 0,0,0

#init pygame
pygame.init()
screen = pygame.display.set_mode(screen_size)

while True:
    screen.fill(background)
    pygame.display.flip()
