#!/usr/bin/python
# coding=utf-8

from modele import Grille
import sys

demineur = Grille(10, 10)
demineur.displayGrid()
demineur.fillGrid('easy')
demineur.playAParty()
