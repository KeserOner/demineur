#!/usr/bin/env python
# coding=utf-8
from modele import Grille

demineur = Grille(5, 5)
demineur.displayGrid()
demineur.fillGrid('easy')
demineur.playAParty()
