#!/usr/bin/python3.4
# coding=utf-8

import pygame
from pygame.locals import *
from modele import Grille
import sys

demineur = Grille(10, 10)
"""demineur.displayGrid()
demineur.fillGrid('easy')
demineur.playAParty()"""
POSX = 150
POSY = 100
SQUARE_SIZE = 30

pygame.init()

main_frame = pygame.display.set_mode((640, 640), RESIZABLE)

background = pygame.image.load('img/grey-background.jpg').convert()
main_frame.blit(background, (0, 0))

backgrd_x = demineur.rows * SQUARE_SIZE
backgrd_y = demineur.column * SQUARE_SIZE

backgrd_rect = Rect(POSX, POSY, backgrd_x, backgrd_y)
pygame.draw.rect(main_frame, Color("white"), backgrd_rect, 0)

font = pygame.font.SysFont('Arial', 10)

rect_x = []
y = 0
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
        main_frame.blit(font.render(str(y), True, (0, 0, 0)), line_y.center)
        y += 1
        pygame.draw.rect(main_frame, Color("black"), line_y, 1)

pygame.display.flip()

continu = True
while continu:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        """if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:"""

    continue
