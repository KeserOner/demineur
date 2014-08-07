#!/usr/bin/python
# coding=utf-8

from modele import Grille
import sys

demineur = Grille(10, 10)
demineur.fillGrid('easy')
demineur.displayGame()
demineur.playAParty()
