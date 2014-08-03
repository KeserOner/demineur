#!/usr/bin/python3.4
# coding=utf-8

import pygame
from pygame.locals import *
from modele import Grille
import sys

demineur = Grille(10, 10)
demineur.displayGrid()
demineur.fillGrid('easy')
demineur.playAParty()

