import pygame
from pygame.locals import *
import sys
import os

#Initialization
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,600))
pygame.display.set_caption("Militant, the Game")
background = pygame.Surface(DISPLAYSURF.get_size()).convert()
background.fill((255,255,255))
screen.blit(DISPLAYSURF, (0,0))

#Information about the different countries
MiddleEast = {damage:20, mobility:15, health:50, defense:20, gold:20, scorepoints:50}
Australia = {damage:40, mobility:25, health:60, defense:30, gold:40, scorepoints:60}
Asia = {damage:50, mobility:30, health:70, defense:40, gold:60, scorepoints:100}
Africa = {damage:70, mobility:20, health:80, defense:40, gold:70, scorepoints:100}
SouthAmerica = {damage:80, mobility:40, health:80, defense:70, gold:90, scorepoints:100}
Europe = {damage:90, mobility:50, health:90, defense:80, gold:95, scorepoints:145}
NorthAmerica = {damage:100, mobility:80, health:100, defense:80, gold:95, scorepoints:145}

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
