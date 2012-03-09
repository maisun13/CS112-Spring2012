#!/usr/bin/ env python

import pygame
import pygame, random
from pygame.locals import *


GREY = 80, 80, 80
WHITE = 150, 150, 150
RED = 255, 0, 0
GREEN = 0, 255, 0
BLACK = 0, 0, 0
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 30
SQ_SIZE = 60, 60
gameover = False
win = False
lose = False
end = False

# Functions

# Draw flag
def draw_flag((x,y)):
    pole = pygame.Rect((x-5,y-20), (5,35))
    pygame.draw.rect(screen, BLACK, pole)
    pygame.draw.polygon(screen, GREEN, [(x,y-20),(x+20,y-10),(x,y)])

# Draw  mines
def draw_mine((p,q)):
    bombtop = pygame.Rect((p-8,q-12),(16,5))
    fuse = pygame.Rect((p-2,q-18),(5,10))
    pygame.draw.circle(screen, BLACK, (p,q+5), 15)
    pygame.draw.rect(screen, BLACK, fuse)
    pygame.draw.rect(screen, GREY, bombtop)

# To enlarge the mines
def rect_grower((x1,y1), (x2,y2), (x3,y3), (x4,y4)):
    x1,y1 = x1 - 5, y1 - 5  # Top left
    x2,y2 = x2 + 5, y2 - 5  # Top Right
    x3,y3 = x3 - 5, y3 + 5  # Bottom Left
    x4,y4 = x4 + 5, y4 + 5  # Bottom Right
    x5,y5 = x1, y1 +15      # Left
    x6,y6 = x2, y2 +15      # Right
    x7,y7 = x3 + 15, y3     # Bottom
    x8,y8 = x1 + 15, y1     # Top

    return [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8)]

# Initializing Screen
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# Objects
bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 40)
bounds = screen.get_rect()
rects = []
clickedlft = []
clickedrt = []
mines = []
boompoints = []
safes = []

 # The grid
for a in range(0,600,60):
    for b in range(0,600,60):
        sq = pygame.Rect((a,b),SQ_SIZE)
        rects.append(sq)
# The mines
mines = random.sample(rects,10)
mines = sorted(mines)
for mine in mines:
    pt = rect_grower(mine.topleft,mine.topright,mine.bottomleft,mine.bottomright)
    boompoints.extend(pt)

# Game Loop
clock = pygame.time.Clock()
done = False
while not done:

    # Input
    for evt in pygame.event.get():
        # Quit
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True

        # Click on rect
        elif evt.type == MOUSEBUTTONDOWN and evt.button == 1:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()) and end == False:
                    clickedlft.append(rect)
                    if rect in clickedrt:
                        clickedrt.remove(rect)
                    if rect in mines:
                        lose = True


        # Flagging
        elif evt.type == MOUSEBUTTONDOWN and evt.button == 3:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()) and rect not in clickedlft and end == False:
                    if rect not in clickedrt:
                        clickedrt.append(rect)
                    elif rect in clickedrt:
                        clickedrt.remove(rect)

    # DRAW
    screen.fill(GREY)

    # Grid
    for rect in rects:
        if rect in clickedlft:
            color = WHITE
        elif rect in mines and end == True:
            color = RED
        else:
            color = GREY
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

    # Flags
    for rect in clickedrt:
        drawFlag(rect.center)
        clickedrt = sorted(clickedrt)

    # Mines
    for rect in mines:
        if rect in clickedlft:
            draw_mine(rect.center)

    # Numbers
    for rect in clickedlft:
        mines_near = 0
        for boompoint in boompoints:
            if rect.collidepoint(boompoint):
                mines_near += 1
        if mines_near > 0 and rect not in mines:
            text = smallfont.render(str(mines_near), True, (0,0,0),WHITE)
            loc = text.get_rect()
            loc.center = rect.center
            screen.blit(text,loc)

    # Clearing multiple spaces
        elif mines_near == 0:
            safe = rect_grower(rect.topleft, rect.topright, rect.bottomleft, rect.bottomright)
            safes.extend(safe)
    for rect in rects:
        for safe in safes:
            if rect.collidepoint(safe) and rect not in clickedlft:
                clickedlft.append(rect)
                safes = []

    
    if clickedrt == mines:
        win = True
    
    # If player wins
    if win == True:
        end = True
        wintext = bigfont.render("YOU'RE A WINNER!", True, (0, 0, 0), GREEN)
        locw = wintext.get_rect()
        locw.center = bounds.center
        screen.blit(wintext, locw)
    
    # If player loses
    if lose == True:
        end = True
        losetext = bigfont.render("YOU'RE A LOSER!", True, (0, 0, 0), GREEN)
        locl = losetext.get_rect()
        locl.center = bounds.center
        screen.blit(losetext, locl)

    # to refresh
    pygame.display.flip()
