#!/usr/bin/python3.4
# coding=utf-8
import pygame
from pygame.locals import *
from modele import Grille

demineur = Grille(10, 10)
"""demineur.displayGrid()
demineur.fillGrid('easy')
demineur.playAParty()"""
POSX = 250
POSY = 200
SQUARE_SIZE = 16
pygame.init()

main_frame = pygame.display.set_mode((640, 640), RESIZABLE)
background = pygame.image.load('img/grey-background.jpg').convert()
main_frame.blit(background, (0, 0))
backgrd_x = demineur.rows * SQUARE_SIZE
backgrd_y = demineur.column * SQUARE_SIZE
backgrd_rect = Rect(POSX, POSY, backgrd_x, backgrd_y)
#test = Rect(SQUARE_SIZE - 1, SQUARE_SIZE - 1, POSX, POSY)
pygame.draw.rect(main_frame, Color("white"), backgrd_rect, 0)
#pygame.draw.rect(main_frame, Color("black"), test, 1)
rect_x = []

i = POSX
while i < POSX + backgrd_x:
    j = POSY
    rect_y = []
    while j < POSY + backgrd_y:
        rect_y.append(Rect(i, j, SQUARE_SIZE - 1, SQUARE_SIZE - 1))
        j += SQUARE_SIZE
    i += SQUARE_SIZE
    rect_x.append(rect_y)

for line_x in rect_x:
    for line_y in line_x:
        pygame.draw.rect(main_frame, Color("black"), line_y, 1)

pygame.display.flip()

continu = 1
while continu:
    continue
