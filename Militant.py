import pygame                                         #### REMOVE MOBILITY ON COUNTRIES; add enemy costs to all country dictionaries
from pygame.locals import *    
import sys
import os

##################################  FUNCTIONS  ##################################
def ally_allocation(countryName, country):
    "draws all elements needed for ally allocation to the game screen"
    allyTextScreen = pygame.image.load("greyRectangle.jpg").convert()
    DISPLAYSURF.blit(allyTextScreen, (300, 430))
    allyMsg = "are you sure you want become allies with {0} for {1} gold coins?".format(countryName, country["allycost"])
    screenText = allyScreenTextFont.render(allyMsg, True, (255, 255, 255))
    DISPLAYSURF.blit(screenText, (320, 440))
    checkButton = pygame.image.load("checkButton.png").convert()
    xButton = pygame.image.load("xButton.jpeg").convert()
    DISPLAYSURF.blit(checkButton, (360, 490))
    DISPLAYSURF.blit(xButton, (520, 490))
    greyRectangle = True
    return greyRectangle

def ally_allocation_confirm(country):
    "Confirmation of ally status; checks if the player has enough gold to afford the ally"
    allyCost = country["allycost"]
    playerGold = playerStat["gold"]
    if allyCost <= playerGold:
        allyCapability = True
    elif allyCost > playerGold:
        allyCapability = False
    return allyCapability

def ally_allocation_execute(country, countryName, damageAdded, healthAdded, defenseAdded):
    "Execution of ally status; perks vary depending on country"
    country["ally"] = True
    country["enemy"] = False
    playerStat["gold"] -= country["allycost"]   #decrease the player's gold amount by the ally cost amount
    playerStat["damage"] += damageAdded         #Increase defense
    playerStat["health"] += healthAdded         #Increase health
    playerStat["defense"] += defenseAdded       #Increase defense
    
def ally_allocation_fail():                         # NOT NECESSARY######
    insufficientFundsMessage = "You do not have enough gold for this ally"
    insufficientFundsText = allyScreenTextFont.render(insufficientFundsMessage, True, (255, 255, 255))
    DISPLAYSURF.blit(insufficientFundsText, (320, 510))

def enemy_allocation(countryName, country):
    "draws all elements needed for enemy allocation to the game screen"
    enemyTextScreen = pygame.image.load("greyRectangle.jpg").convert()
    DISPLAYSURF.blit(enemyTextScreen, (300, 430))
    enemyMsg = "are you sure you want become enemies with {0} for {1} coins?".format(countryName, country["enemycost"])
    enemyStatsMsg = "The enemy has: Damage: {0} Health: {1}  Defense: {2}  Gold Reward: {3}".format(country["damage"], country["health"], country["defense"], country["gold"]) 
    screenText = enemyScreenTextFont.render(enemyMsg, True, (255, 255, 255))
    DISPLAYSURF.blit(screenText, (305, 440))
    screenTextStatsMsg = enemyScreenTextFont.render(enemyStatsMsg, True, (255, 255, 255))
    DISPLAYSURF.blit(screenTextStatsMsg, (290, 460))
    checkButton = pygame.image.load("checkButton.png").convert()
    xButton = pygame.image.load("xButton.jpeg").convert()
    DISPLAYSURF.blit(checkButton, (360, 490))
    DISPLAYSURF.blit(xButton, (520, 490))
    greyRectangle = True
    return greyRectangle

def enemy_allocation_confirm(country):
    "Confirmation of enemy status; checks if the player has enough gold to afford the enemy"
    enemyCost = country["enemycost"]
    playerGold = playerStat["gold"]
    if enemyCost <= playerGold:
        enemyCapability = True
    elif enemyCost > playerGold:
        enemyCapability = False
    return enemyCapability

def enemy_allocation_execute(country):
    "Attacks the designated country; decreases enemys defense and health by the players attack amount"
    if country["damage"] > playerStat["defense"]:
        damageFloodtoHealth = country["damage"] - playerStat["defense"]
        playerStat["defense"] = 0
        playerStat["health"] -= damageFloodtoHealth
    else:
        playerStat["defense"] -= country["damage"]
    playerStat["gold"] -= country["enemycost"]
    country["ally"] = False
    country["enemy"] = True

def mainGameScreen():
    "Draws the main game screen to the display surface"
    mainGameScreen = pygame.image.load("Worldmap.gif")
    DISPLAYSURF = pygame.display.set_mode(mainGameScreen.get_size())
    mainGameScreen = mainGameScreen.convert()
    DISPLAYSURF.blit(mainGameScreen, (0, 0))
    background_variable = "mainGameScreen"

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

    #draws the stats box to the screen
    playerStatBox = pygame.image.load("playerStatBox.gif").convert()
    DISPLAYSURF.blit(playerStatBox, (730, 450))
    return background_variable

def game_lose():
    "Draws a rectangle to the screen saying the player has lost the game"
    greyRectangle_game_lose = pygame.image.load("greyRectangle.jpg").convert()
    DISPLAYSURF.blit(greyRectangle_game_lose, (300, 200))
    game_lose_msg = "You lose"
    game_lose_Text = game_lose_ScreenTextFont.render(game_lose_msg, True, (0, 0, 0))
    DISPLAYSURF.blit(game_lose_Text, (410, 250))
    game_lose_line2_msg = "Press the exit button to quit the game"
    game_lose_line2_Text = game_lose_ScreenTextFont.render(game_lose_line2_msg, True, (0, 0, 0))
    DISPLAYSURF.blit(game_lose_line2_Text, (300, 270))

##############################################################################

#Initialization
pygame.init()
startingScreen = pygame.image.load("startingscreen.gif")
DISPLAYSURF = pygame.display.set_mode(startingScreen.get_size())
startingScreen = startingScreen.convert()
pygame.display.set_caption("Militant, the Game")
DISPLAYSURF.blit(startingScreen, (0, 0))
pygame.display.flip()

#fonts
allyScreenTextFont = pygame.font.SysFont(None, 15)
enemyScreenTextFont = pygame.font.SysFont(None, 15)
game_lose_ScreenTextFont = pygame.font.SysFont(None, 25)

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
MiddleEast = {"damage": 20, "health": 50, "defense": 20, "gold": 20, "scorepoints": 50, "enemy": False, "ally": False, "allycost": 80}
Australia = {"damage": 40, "health": 60, "defense": 30, "gold": 40, "scorepoints": 60, "enemy": False, "ally": False, "allycost": 30}
Asia = {"damage": 50, "health":70, "defense":40, "gold":60, "scorepoints":100, "enemy": False, "ally": False, "allycost": 40}
Africa = {"damage": 70, "health":80, "defense":40, "gold":70, "scorepoints":100, "enemy": False, "ally": False, "allycost": 30, "enemycost": 10}
SouthAmerica = {"damage":80, "health": 80, "defense": 70, "gold": 90, "scorepoints": 100, "enemy": False, "ally": False, "allycost": 100}
Europe = {"damage": 90, "health": 90, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False, "allycost": 100}
NorthAmerica = {"damage": 100, "health": 100, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False, "allycost": 150}

#Information about the player
playerStat = {"damage": 40, "health": 40, "defense": 40, "gold": 50, "scorepoints": 0}

#clock information
clock = pygame.time.Clock()

#Initialization for checking variables; used for events in the main game screen
background_variable = "startingScreen"
initial_Variable = 0

#Initialization for the grey rectangles (7 grey rectangles for each allocations; 14 rectangles total)
greyRectangleAfrica_Ally, greyRectangleMiddleEast_Ally, greyRectangleAsia_Ally, greyRectangleAustralia_Ally, greyRectangleSouthAmerica_Ally, greyRectangleNorthAmerica_Ally, greyRectangleEurope_Ally = (False,)*7
greyRectangleAfrica_Enemy, greyRectangleMiddleEast_Enemy, greyRectangleAsia_Enemy, greyRectangleAustralia_Enemy, greyRectangleSouthAmerica_Enemy, greyRectangleNorthAmerica_Enemy, greyRectangleEurope_Enemy = (False,)*7

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if initial_Variable == 0 and event.type == KEYDOWN:
            #Main game screen information
            mainGameScreen()
            initial_Variable += 1

        elif initial_Variable == 1:
            #events for mouse events
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                ############################  ALLY ALLOCATION  ############################
                
                #Ally status allocation for Africa
                if ((480 + ally_Button_Length) > pos[0] > 480) and ((240 + ally_Button_Width) > pos[1] > 240):
                    ally_allocation("Africa", Africa)
                    greyRectangleAfrica_Ally = ally_allocation("Africa", Africa)
                elif greyRectangleAfrica_Ally == True:                                   #Checks if returned value from function is true
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        ally_allocation_confirm(Africa)
                        allyCapability = ally_allocation_confirm(Africa)
                        if allyCapability == True:
                            print(playerStat)
                            ally_allocation_execute(Africa, "Africa", 20, 10, 10)
                            print(playerStat)
                            greyRectangleAfrica_Ally = False
                            mainGameScreen()
                        elif allyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleAfrica_Ally = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleAfrica_Ally = False
                        
                #Ally status allocation for Middle East             
                elif ((580 + ally_Button_Length) > pos[0] > 580) and ((185 + ally_Button_Width) > pos[1] > 185):
                    ally_allocation("the Middle East", MiddleEast)
                    greyRectangleMiddleEast_Ally = ally_allocation("the Middle East", MiddleEast)
                elif greyRectangleMiddleEast_Ally == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        ally_allocation_confirm(MiddleEast)
                        allyCapability = ally_allocation_confirm(MiddleEast)
                        if allyCapability == True:
                            print(playerStat)
                            ally_allocation_execute(MiddleEast, "the Middle East", 0, 20, 5)
                            print(playerStat)
                            greyRectangleMiddleEast_Ally = False
                            mainGameScreen()
                        elif allyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleMiddleEast_Ally = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleMiddleEast_Ally = False
                        
                #Ally status allocation for Asia 
                elif ((660 + ally_Button_Length) > pos[0] > 660) and ((120 + ally_Button_Width) > pos[1] > 120):      
                    ally_allocation("Asia", Asia)
                    greyRectangleAsia_Ally = ally_allocation("Asia", Asia)
                elif greyRectangleAsia_Ally == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        ally_allocation_confirm(Asia)
                        allyCapability = ally_allocation_confirm(Asia)
                        if allyCapability == True:
                            print(playerStat)
                            ally_allocation_execute(Asia, "Asia", 15, 20, 10)
                            print(playerStat)
                            greyRectangleAsia_Ally = False
                            mainGameScreen()
                        elif allyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleAsia_Ally = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleAsia_Ally = False
                   
                #Ally status allocation for Australia
                elif ((810 + ally_Button_Length) > pos[0] > 810) and ((375 + ally_Button_Width) > pos[1] > 375):      
                    ally_allocation("Australia", Australia)
                    greyRectangleAustralia_Ally = ally_allocation("Australia", Australia)
                elif greyRectangleAustralia_Ally == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        ally_allocation_confirm(Australia)
                        allyCapability = ally_allocation_confirm(Australia)
                        if allyCapability == True:
                            print(playerStat)
                            ally_allocation_execute(Australia, "Australia", 10, 20, 10)
                            print(playerStat)
                            greyRectangleAustralia_Ally = False
                            mainGameScreen()
                        elif allyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleAustralia_Ally = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleAustralia_Ally = False
                    
                #Ally status allocation for South America
                elif ((265 + ally_Button_Length) > pos[0] > 265) and ((330 + ally_Button_Width) > pos[1] > 330): 
                    ally_allocation("South America", SouthAmerica)
                    greyRectangleSouthAmerica_Ally = ally_allocation("South America", SouthAmerica)
                elif greyRectangleSouthAmerica_Ally == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        ally_allocation_confirm(SouthAmerica)
                        allyCapability = ally_allocation_confirm(SouthAmerica)
                        if allyCapability == True:
                            print(playerStat)
                            ally_allocation_execute(SouthAmerica, "South America", 30, 30, 20)
                            print(playerStat)
                            greyRectangleSouthAmerica_Ally = False
                            mainGameScreen()
                        elif allyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleSouthAmerica_Ally = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleSouthAmerica_Ally = False
                    
                #Ally status allocation for North America
                elif ((150 + ally_Button_Length) > pos[0] > 150) and ((165 + ally_Button_Width) > pos[1] > 165):   
                    ally_allocation("North America", NorthAmerica)
                    greyRectangleSouthAmerica_Ally = ally_allocation("North America", NorthAmerica)
                elif greyRectangleNorthAmerica_Ally == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        ally_allocation_confirm(NorthAmerica)
                        allyCapability = ally_allocation_confirm(NorthAmerica)
                        if allyCapability == True:
                            print(playerStat)
                            ally_allocation_execute(NorthAmerica, "North America", 50, 50, 40)
                            print(playerStat)
                            greyRectangleNorthAmerica_Ally = False
                            mainGameScreen()
                        elif allyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleNorthAmerica_Ally = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleNorthAmerica_Ally = False
                    
                #Ally status allocation for Europe
                elif ((510 + ally_Button_Length) > pos[0] > 510) and ((125 + ally_Button_Width) > pos[1] > 125):   
                    ally_allocation("Europe", Europe)
                    greyRectangleEurope_Ally = ally_allocation("Europe", Europe)
                elif greyRectangleEurope_Ally == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        ally_allocation_confirm(Europe)
                        allyCapability = ally_allocation_confirm(Europe)
                        if allyCapability == True:
                            print(playerStat)
                            ally_allocation_execute(Europe, "Europe", 40, 40, 30)
                            print(playerStat)
                            greyRectangleEurope_Ally = False
                            mainGameScreen()
                        elif allyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleEurope_Ally = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleEurope_Ally = False
                    
                ###########################################################################

                ############################  ENEMY ALLOCATION  ###########################
                        
                #Enemy status allocation for Africa
                elif ((440 + enemy_Button_Length) > pos[0] > 440) and ((240 + enemy_Button_Width) > pos[1] > 240):
                    enemy_allocation("Africa", Africa)
                    greyRectangleAfrica_Enemy = enemy_allocation("Africa", Africa)
                elif greyRectangleAfrica_Enemy == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        enemy_allocation_confirm(Africa)
                        enemyCapability = enemy_allocation_confirm(Africa)
                        if enemyCapability == True:
                            print("beginning player stat: ", playerStat)
                            print("beginning enemy stat: ", Africa)
                            enemy_allocation_execute(Africa)    #enemy_allocation_execute(Asia, "Asia", 15, 10, 20, 10)
                            print("ending player stat: ", playerStat)
                            print("ending enemy stat: ", Africa)
                            greyRectangleAfrica_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this ally")
                            greyRectangleAfrica_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleAfrica_Enemy = False
                        
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

            #Check if the player has lost the game
            elif playerStat["health"] <= 0 :
                game_lose()
                if event.type == QUIT:
                    pygame.display.quit()
                    sys.exit()

            #If the player chooses to exit the game
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()

        #Update the game screen
        pygame.display.flip()
        pygame.display.update()


