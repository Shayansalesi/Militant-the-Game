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
DISPLAYSURF.blit(startingscreen, (0, 0))
pygame.display.flip()

#ally button dimensions
ally_Button_Length = pygame.image.load("allybutton.jpg").get_rect().size[0]
ally_Button_Width = pygame.image.load("allybutton.jpg").get_rect().size[1]

#Enemy button dimensions
enemy_Button_Length = pygame.image.load("attackbutton.png").get_rect().size[0]
enemy_Button_Width = pygame.image.load("attackbutton.png").get_rect().size[1]

#Information about the different countries
MiddleEast = {"damage": 20, "mobility": 15, "health": 50, "defense": 20, "gold": 20, "scorepoints": 50, "enemy": False, "ally": False}
Australia = {"damage": 40, "mobility": 25, "health": 60, "defense": 30, "gold": 40, "scorepoints": 60, "enemy": False, "ally": False}
Asia = {"damage": 50, "mobility": 30, "health":70, "defense":40, "gold":60, "scorepoints":100, "enemy": False, "ally": False}
Africa = {"damage": 70, "mobility": 20, "health":80, "defense":40, "gold":70, "scorepoints":100, "enemy": False, "ally": False}
SouthAmerica = {"damage":80, "mobility": 40, "health": 80, "defense": 70, "gold": 90, "scorepoints": 100, "enemy": False, "ally": False}
Europe = {"damage": 90, "mobility": 50, "health": 90, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False}
NorthAmerica = {"damage": 100, "mobility": 80, "health": 100, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False}

#Information about the player
playerStat = {"damage": 100, "mobility": 100, "health": 100, "defense": 100, "gold": 100, "scorepoints": 0}

#clock information
clock = pygame.time.Clock()

#Initialization for checking variables; used for events in the main game screen
background_variable = 0
firstBootScreen = pygame.image.load("Worldmap.gif")
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #Main game screen information
            firstBootScreen = pygame.image.load("Worldmap.gif")
            DISPLAYSURF = pygame.display.set_mode(firstBootScreen.get_size())
            firstBootScreen = firstBootScreen.convert()
            DISPLAYSURF.blit(firstBootScreen, (0, 0))
            background_variable = firstBootScreen

        if background_variable == firstBootScreen:
            #Ally button locations
            ally_Button_Africa = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Africa, (480, 240))
            ally_Button_MiddleEast = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_MiddleEast, (580, 185))
            ally_Button_Asia = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Asia, (660, 120))
            ally_Button_Australia = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Australia, (810, 375))
            ally_Button_SouthAmerica = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_SouthAmerica, (265, 330))
            ally_Button_NorthAmerica = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_NorthAmerica, (150, 165))
            ally_Button_Europe = pygame.image.load("allybutton.jpg").convert()
            DISPLAYSURF.blit(ally_Button_Europe, (510, 125))

            #Enemy button locations
            Enemy_Button_Africa = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Africa, (440, 240))
            Enemy_Button_MiddleEast = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_MiddleEast, (540, 185))
            Enemy_Button_Asia = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Asia, (620, 120))
            Enemy_Button_Australia = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Australia, (770, 375))
            Enemy_Button_SouthAmerica = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_SouthAmerica, (225, 330))
            Enemy_Button_NorthAmerica = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_NorthAmerica, (110, 165))
            Enemy_Button_Europe = pygame.image.load("attackbutton.png").convert()
            DISPLAYSURF.blit(Enemy_Button_Europe, (470, 125))

            #events for mouse events
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ############################  ALLY ALLOCATION  ############################
                #Ally status allocation for Africa
                if ((480 + ally_Button_Length) > pos[0] > 480) and ((240 + ally_Button_Width) > pos[1] > 240):
                    for key in Africa.keys():
                        if key == "ally":
                            Africa[key] = True  #Set ally key to True; subtract from players gold
                #Ally status allocation for Middle East
                if ((580 + ally_Button_Length) > pos[0] > 580) and ((185 + ally_Button_Width) > pos[1] > 185):
                    for key in MiddleEast.keys():
                        if key == "ally":
                            MiddleEast[key] = True  
                #Ally status allocation for Asia 
                if ((660 + ally_Button_Length) > pos[0] > 660) and ((120 + ally_Button_Width) > pos[1] > 120):
                    for key in Asia.keys():
                        if key == "ally":
                            Asia[key] = True
                #Ally status allocation for Australia
                if ((810 + ally_Button_Length) > pos[0] > 810) and ((375 + ally_Button_Width) > pos[1] > 375):
                    for key in Australia.keys():
                        if key == "ally":
                            Australia[key] = True  
                #Ally status allocation for South America
                if ((265 + ally_Button_Length) > pos[0] > 265) and ((330 + ally_Button_Width) > pos[1] > 330):
                    for key in SouthAmerica.keys():
                        if key == "ally":
                            SouthAmerica[key] = True  
                #Ally status allocation for North America
                if ((150 + ally_Button_Length) > pos[0] > 150) and ((165 + ally_Button_Width) > pos[1] > 165):
                    for key in NorthAmerica.keys():
                        if key == "ally":
                            NorthAmerica[key] = True  
                #Ally status allocation for Europe
                if ((510 + ally_Button_Length) > pos[0] > 510) and ((125 + ally_Button_Width) > pos[1] > 125):
                    for key in Europe.keys():
                        if key == "ally":
                            Europe[key] = True  
                ###########################################################################

                ############################  ENEMY ALLOCATION  ###########################
                #Enemy status allocation for Africa
                if ((440 + enemy_Button_Length) > pos[0] > 440) and ((240 + enemy_Button_Width) > pos[1] > 240):
                    for key in Africa.keys():
                        if key == "enemy":
                            Africa[key] = True  #Set enemy key to True; subtract from players gold
                #Enemy status allocation for Middle east
                if ((540 + enemy_Button_Length) > pos[0] > 540) and ((185 + enemy_Button_Width) > pos[1] > 185):
                    for key in MiddleEast.keys():
                        if key == "enemy":
                            MiddleEast[key] = True  
                #Enemy status allocation for Asia
                if ((620 + enemy_Button_Length) > pos[0] > 620) and ((120 + enemy_Button_Width) > pos[1] > 120):
                    for key in Asia.keys():
                        if key == "enemy":
                            Asia[key] = True  
                #Enemy status allocation for Australia
                if ((770 + enemy_Button_Length) > pos[0] > 770) and ((375 + enemy_Button_Width) > pos[1] > 375):
                    for key in Australia.keys():
                        if key == "enemy":
                            Australia[key] = True  
                #Enemy status allocation for South America
                if ((225 + enemy_Button_Length) > pos[0] > 225) and ((330 + enemy_Button_Width) > pos[1] > 330):
                    for key in SouthAmerica.keys():
                        if key == "enemy":
                            SouthAmerica[key] = True  
                #Enemy status allocation for North america
                if ((110 + enemy_Button_Length) > pos[0] > 110) and ((165 + enemy_Button_Width) > pos[1] > 165):
                    for key in NorthAmerica.keys():
                        if key == "enemy":
                            NorthAmerica[key] = True  
                #Enemy status allocation for Europe
                if ((470 + enemy_Button_Length) > pos[0] > 470) and ((125 + enemy_Button_Width) > pos[1] > 125):
                    for key in Europe.keys():
                        if key == "enemy":
                            Europe[key] = True  
                ###########################################################################

            #If the player chooses to exit the game
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        #Update the game screen
        pygame.display.flip()
        pygame.display.update()

