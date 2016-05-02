import pygame
from pygame.locals import *
import sys
import os

#Initialization
pygame.init()
startingscreen = pygame.image.load("startingscreen.gif")
DISPLAYSURF = pygame.display.set_mode(startingscreen.get_size())
startingscreen = startingscreen.convert()
pygame.display.set_caption("Militant, the Game")
DISPLAYSURF.blit(startingscreen,(0,0))
pygame.display.flip()


#Information about the different countries
MiddleEast = {"damage":20, "mobility":15, "health":50, "defense":20, "gold":20, "scorepoints":50}
Australia = {"damage":40, "mobility":25, "health":60, "defense":30, "gold":40, "scorepoints":60}
Asia = {"damage":50, "mobility":30, "health":70, "defense":40, "gold":60, "scorepoints":100}
Africa = {"damage":70, "mobility":20, "health":80, "defense":40, "gold":70, "scorepoints":100}
SouthAmerica = {"damage":80, "mobility":40, "health":80, "defense":70, "gold":90, "scorepoints":100}
Europe = {"damage":90, "mobility":50, "health":90, "defense":80, "gold":95, "scorepoints":145}
NorthAmerica = {"damage":100, "mobility":80, "health":100, "defense":80, "gold":95, "scorepoints":145}

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #Main game screen information
            firstBootScreen = pygame.image.load("Worldmap.gif")
            DISPLAYSURF = pygame.display.set_mode(firstBootScreen.get_size())
            firstBootScreen = firstBootScreen.convert()
            DISPLAYSURF.blit(firstBootScreen,(0,0))
            pygame.display.flip()                       
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

