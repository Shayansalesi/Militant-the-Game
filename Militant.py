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

#Information about the player
playerStat = {"damage":100, "mobility":100, "health":100, "defense":100, "gold":100, "scorepoints":0}

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #Main game screen information
            firstBootScreen = pygame.image.load("Worldmap.gif")
            DISPLAYSURF = pygame.display.set_mode(firstBootScreen.get_size())
            firstBootScreen = firstBootScreen.convert()
            DISPLAYSURF.blit(firstBootScreen,(0,0))
            
            #Ally button locations
            ally_Button_Africa = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Africa,(480,240))
            ally_Button_MiddleEast = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_MiddleEast,(580,185))
            ally_Button_Asia = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Asia,(660,120))
            ally_Button_Australia = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Australia,(810,375))
            ally_Button_SouthAmerica = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_SouthAmerica,(265,330))
            ally_Button_NorthAmerica = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_NorthAmerica,(150,165))
            ally_Button_Europe = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Europe,(510,125))

            #Enemy button locations
            Enemy_Button_Africa = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Africa,(440,240))
            Enemy_Button_MiddleEast = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_MiddleEast,(540,185))
            Enemy_Button_Asia = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Asia,(620,120))
            Enemy_Button_Australia = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Australia,(770,375))
            Enemy_Button_SouthAmerica = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_SouthAmerica,(225,330))
            Enemy_Button_NorthAmerica = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_NorthAmerica,(110,165))
            Enemy_Button_Europe = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Europe,(470,125))

        #If the player chooses to exit the game
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Update the game screen
        pygame.display.flip()
        pygame.display.update()

