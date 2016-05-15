import pygame
from pygame.locals import *
import sys
import os

###################  FUNCTIONS  ###################
def ally_allocation(country, countryName, damageAdded, mobilityAdded, healthAdded, defenseAdded):
    #Sets the status of a country to ally if it can be afforded
    allyCost = country["allycost"]
    playerGold = playerStat["gold"]
    allyTicker = True
    if allyTicker == True:   #To time the amount of time the rectangular option box shows
        allyTextScreen = pygame.image.load("greyRectangle.jpg").convert()
        DISPLAYSURF.blit(allyTextScreen, (300, 430))
        allyMsg = "are you sure you want become allies with {0} for {1} gold coins?".format(countryName, country["allycost"])
        screenText = allyScreenTextFont.render(allyMsg, True, (255, 255, 255))
        DISPLAYSURF.blit(screenText, (320, 440))
        checkButton = pygame.image.load("checkButton.png").convert()
        xButton = pygame.image.load("xButton.jpeg").convert()
        DISPLAYSURF.blit(checkButton, (360, 490))
        DISPLAYSURF.blit(xButton, (520, 490))    
        if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
            if allyCost < playerGold:
                country["ally"] = True
                playerStat["gold"] -= country["allycost"]   #decrease the player's gold amount by the ally cost amount
                playerStat["damage"] += damageAdded         #Increase defense
                playerStat["mobility"] += mobilityAdded     #Increase mobility
                playerStat["health"] += healthAdded         #Increase health
                playerStat["defense"] += defenseAdded       #Increase defense
                allyTicker = False
            else:
                insufficientFundsMessage = "You do not have enough gold for this ally"
                insufficientFundsText = allyScreenTextFont.render(insufficientFundsMessage, True, (255, 255, 255))
                DISPLAYSURF.blit(insufficientFundsText, (320, 510))
        elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
            country["ally"] = False
            allyTicker = False

def enemy_allocation(country):
    #Sets the status of a country to enemy
        country["enemy"] = True  #Set enemy key to True; subtract from players gold

#Initialization
pygame.init()
startingscreen = pygame.image.load("startingscreen.gif")
DISPLAYSURF = pygame.display.set_mode(startingscreen.get_size())
startingscreen = startingscreen.convert()
pygame.display.set_caption("Militant, the Game")
DISPLAYSURF.blit(startingscreen, (0, 0))
pygame.display.flip()

#font
allyScreenTextFont = pygame.font.SysFont(None, 15)

#x and check button dimensions
x_Button_Length = pygame.image.load("xButton.jpeg").get_rect().size[0]
x_Button_Width = pygame.image.load("xButton.jpeg").get_rect().size[1]
check_Button_Length = pygame.image.load("checkButton.png").get_rect().size[0]
check_Button_Width = pygame.image.load("checkButton.png").get_rect().size[1]

#ally button dimensions
ally_Button_Length = pygame.image.load("allybutton.jpg").get_rect().size[0]
ally_Button_Width = pygame.image.load("allybutton.jpg").get_rect().size[1]

#Enemy button dimensions
enemy_Button_Length = pygame.image.load("attackbutton.png").get_rect().size[0]
enemy_Button_Width = pygame.image.load("attackbutton.png").get_rect().size[1]

#Information about the different countries
MiddleEast = {"damage": 20, "mobility": 15, "health": 50, "defense": 20, "gold": 20, "scorepoints": 50, "enemy": False, "ally": False, "allycost": 80}
Australia = {"damage": 40, "mobility": 25, "health": 60, "defense": 30, "gold": 40, "scorepoints": 60, "enemy": False, "ally": False, "allycost": 60}
Asia = {"damage": 50, "mobility": 30, "health":70, "defense":40, "gold":60, "scorepoints":100, "enemy": False, "ally": False, "allycost": 40}
Africa = {"damage": 70, "mobility": 20, "health":80, "defense":40, "gold":70, "scorepoints":100, "enemy": False, "ally": False, "allycost": 60}
SouthAmerica = {"damage":80, "mobility": 40, "health": 80, "defense": 70, "gold": 90, "scorepoints": 100, "enemy": False, "ally": False, "allycost": 100}
Europe = {"damage": 90, "mobility": 50, "health": 90, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False, "allycost": 100}
NorthAmerica = {"damage": 100, "mobility": 80, "health": 100, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False, "allycost": 150}

#Information about the player
playerStat = {"damage": 40, "mobility": 40, "health": 40, "defense": 40, "gold": 50, "scorepoints": 0}

#clock information
clock = pygame.time.Clock()

#Initialization for checking variables; used for events in the main game screen
background_variable = 0
firstBootScreen = pygame.image.load("Worldmap.gif")
initial_Variable = 0
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if initial_Variable == 0 and event.type == KEYDOWN:
            #Main game screen information
            firstBootScreen = pygame.image.load("Worldmap.gif")
            DISPLAYSURF = pygame.display.set_mode(firstBootScreen.get_size())
            firstBootScreen = firstBootScreen.convert()
            DISPLAYSURF.blit(firstBootScreen, (0, 0))
            background_variable = firstBootScreen
            initial_Variable += 1

        elif background_variable == firstBootScreen:
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
                    ally_allocation(Africa, "Africa", 20, 0, 10, 10)
                    print(playerStat)
                #Ally status allocation for Middle East
                elif ((580 + ally_Button_Length) > pos[0] > 580) and ((185 + ally_Button_Width) > pos[1] > 185):
                    ally_allocation(MiddleEast, "the Middle East", 0, 5, 20, 5) 
                #Ally status allocation for Asia 
                elif ((660 + ally_Button_Length) > pos[0] > 660) and ((120 + ally_Button_Width) > pos[1] > 120):
                    ally_allocation(Asia, "Asia", 15, 10, 20, 10)
                #Ally status allocation for Australia
                elif ((810 + ally_Button_Length) > pos[0] > 810) and ((375 + ally_Button_Width) > pos[1] > 375):
                    ally_allocation(Australia, "Australia", 10, 10, 20, 10)  
                #Ally status allocation for South America
                elif ((265 + ally_Button_Length) > pos[0] > 265) and ((330 + ally_Button_Width) > pos[1] > 330):
                    ally_allocation(SouthAmerica, "South America", 30, 10, 30, 20)  
                #Ally status allocation for North America
                elif ((150 + ally_Button_Length) > pos[0] > 150) and ((165 + ally_Button_Width) > pos[1] > 165):
                    ally_allocation(NorthAmerica, "North America", 50, 40, 50, 40)  
                #Ally status allocation for Europe
                elif ((510 + ally_Button_Length) > pos[0] > 510) and ((125 + ally_Button_Width) > pos[1] > 125):
                    ally_allocation(Europe, "Europe", 40, 30, 40, 30)  
                ###########################################################################

                ############################  ENEMY ALLOCATION  ###########################
                #Enemy status allocation for Africa
                elif ((440 + enemy_Button_Length) > pos[0] > 440) and ((240 + enemy_Button_Width) > pos[1] > 240):
                    enemy_allocation(Africa)
                #Enemy status allocation for Middle east
                elif ((540 + enemy_Button_Length) > pos[0] > 540) and ((185 + enemy_Button_Width) > pos[1] > 185):
                    enemy_allocation(MiddleEast)  
                #Enemy status allocation for Asia
                elif ((620 + enemy_Button_Length) > pos[0] > 620) and ((120 + enemy_Button_Width) > pos[1] > 120):
                    enemy_allocation(Asia)  
                #Enemy status allocation for Australia
                elif ((770 + enemy_Button_Length) > pos[0] > 770) and ((375 + enemy_Button_Width) > pos[1] > 375):
                    enemy_allocation(Australia)
                #Enemy status allocation for South America
                elif ((225 + enemy_Button_Length) > pos[0] > 225) and ((330 + enemy_Button_Width) > pos[1] > 330):
                    enemy_allocation(SouthAmerica)  
                #Enemy status allocation for North america
                elif ((110 + enemy_Button_Length) > pos[0] > 110) and ((165 + enemy_Button_Width) > pos[1] > 165):
                    enemy_allocation(NorthAmerica)  
                #Enemy status allocation for Europe
                elif ((470 + enemy_Button_Length) > pos[0] > 470) and ((125 + enemy_Button_Width) > pos[1] > 125):
                    enemy_allocation(Europe) 
                ###########################################################################

            #If the player chooses to exit the game
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        #Update the game screen
        pygame.display.flip()
        pygame.display.update()
