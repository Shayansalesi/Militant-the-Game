import pygame                                         ####make sure all enemy buttons work 
from pygame.locals import *    
import sys
import os

##################################  FUNCTIONS  ##################################

def ally_allocation(countryName, country, damagetobeAdded, healthtobeAdded, defensetobeAdded):
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
    
    #Draws the red ally stat box with perks to be added
    allyStatBox = pygame.image.load("countryStatBox.gif").convert()
    DISPLAYSURF.blit(allyStatBox, (0,470))
    allyPerksMsg = "Ally Perks"
    damageMsg = "Damage+: {0}".format(damagetobeAdded)
    healthMsg = "Health+: {0}".format(healthtobeAdded)
    defenseMsg = "Defense+: {0}".format(defensetobeAdded)
    allyPerksMsg_Text = statBoxTextFont.render(allyPerksMsg, True, (0, 255, 0))
    damageMsg_Text = statBoxTextFont.render(damageMsg, True, (0, 255, 0))
    healthMsg_Text = statBoxTextFont.render(healthMsg, True, (0, 255, 0))
    defenseMsg_Text = statBoxTextFont.render(defenseMsg, True, (0, 255, 0))
    DISPLAYSURF.blit(allyPerksMsg_Text, (40, 480))
    DISPLAYSURF.blit(damageMsg_Text, (10, 500))
    DISPLAYSURF.blit(healthMsg_Text, (10, 520))
    DISPLAYSURF.blit(defenseMsg_Text, (10, 540))
    
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
    enemyMsg = "are you sure you want to become enemies with {0} for {1} gold coins?".format(countryName, country["enemycost"])
    enemyStatsMsg = "The enemy has: Damage: {0} Health: {1}  Defense: {2}  Gold Reward: {3}".format(country["damage"], country["health"], country["defense"], country["gold"]) 
    screenText = enemyScreenTextFont.render(enemyMsg, True, (255, 255, 255))
    DISPLAYSURF.blit(screenText, (290, 440))
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
    if country["damage"] > playerStat["defense"]:                                   #executes code block if enemy country has higher damage then the player's health
        country_DamageFloodtoHealth = country["damage"] - playerStat["defense"]
        playerStat["defense"] = 0
        playerStat["health"] -= country_DamageFloodtoHealth
    else:
        playerStat["defense"] -= country["damage"]                                  #executes code block if enemy country has lower damage then the player's health
        
    if playerStat["damage"] > country["defense"]:                                   #executes code block if player has higher damage then the country's health
        playerStat_DamageFloodtoHealth = playerStat["damage"] - country["defense"]
        country["defense"] = 0
        country["health"] -= playerStat_DamageFloodtoHealth
    else:
        country["defense"] -= playerStat["damage"]                                  #executes code block if player has lower damage then the country's health
            
    playerStat["gold"] -= country["enemycost"]
    country["ally"] = False
    country["enemy"] = True

def mainGameScreen():
    "Draws the main game screen to the display surface"
    #Main Game Screen
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
    playerStatBox = pygame.image.load("playerStatBox.png").convert()
    DISPLAYSURF.blit(playerStatBox, (700, 470))
    
    #draws player stats onto stat box
    damageMsg = "Damage: {0}".format(playerStat["damage"])
    healthMsg = "Health: {0}".format(playerStat["health"])
    defenseMsg = "Defense: {0}".format(playerStat["defense"])
    goldMsg = "gold: {0}".format(playerStat["gold"])
    damageMsg_Text = statBoxTextFont.render(damageMsg, True, (0, 255, 0))
    healthMsg_Text = statBoxTextFont.render(healthMsg, True, (0, 255, 0))
    defenseMsg_Text = statBoxTextFont.render(defenseMsg, True, (0, 255, 0))
    goldMsg_Text = statBoxTextFont.render(goldMsg, True, (0, 255, 0))
    DISPLAYSURF.blit(damageMsg_Text, (710, 480))
    DISPLAYSURF.blit(healthMsg_Text, (710, 500))
    DISPLAYSURF.blit(defenseMsg_Text, (710, 520))
    DISPLAYSURF.blit(goldMsg_Text, (710, 540))
                                   
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
statBoxTextFont = pygame.font.SysFont(None, 20)

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
MiddleEast = {"damage": 20, "health": 50, "defense": 20, "gold": 20, "scorepoints": 50, "enemy": False, "ally": False, "allycost": 80, "enemycost": 10}
Australia = {"damage": 40, "health": 60, "defense": 30, "gold": 40, "scorepoints": 60, "enemy": False, "ally": False, "allycost": 30, "enemycost": 10}
Asia = {"damage": 50, "health":70, "defense":40, "gold":60, "scorepoints":100, "enemy": False, "ally": False, "allycost": 40, "enemycost": 10}
Africa = {"damage": 70, "health":80, "defense":40, "gold":70, "scorepoints":100, "enemy": False, "ally": False, "allycost": 30, "enemycost": 10}
SouthAmerica = {"damage":80, "health": 80, "defense": 70, "gold": 90, "scorepoints": 100, "enemy": False, "ally": False, "allycost": 100, "enemycost": 10}
Europe = {"damage": 90, "health": 90, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False, "allycost": 100, "enemycost": 10}
NorthAmerica = {"damage": 100, "health": 100, "defense": 80, "gold": 95, "scorepoints": 145, "enemy": False, "ally": False, "allycost": 150, "enemycost": 10}

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
                    ally_allocation("Africa", Africa, 20, 10, 10)
                    greyRectangleAfrica_Ally = ally_allocation("Africa", Africa, 20, 10, 10)
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
                    ally_allocation("the Middle East", MiddleEast, 0, 20, 5)
                    greyRectangleMiddleEast_Ally = ally_allocation("the Middle East", MiddleEast, 0, 20, 5)
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
                    ally_allocation("Asia", Asia, 15, 20, 10)
                    greyRectangleAsia_Ally = ally_allocation("Asia", Asia, 15, 20, 10)
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
                    ally_allocation("Australia", Australia, 10, 20, 10)
                    greyRectangleAustralia_Ally = ally_allocation("Australia", Australia, 10, 20, 10)
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
                    ally_allocation("South America", SouthAmerica, 30, 30, 20)
                    greyRectangleSouthAmerica_Ally = ally_allocation("South America", SouthAmerica, 30, 30, 20)
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
                    ally_allocation("North America", NorthAmerica, 50, 50, 40)
                    greyRectangleSouthAmerica_Ally = ally_allocation("North America", NorthAmerica, 50, 50, 40)
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
                    ally_allocation("Europe", Europe, 40, 40, 30)
                    greyRectangleEurope_Ally = ally_allocation("Europe", Europe, 40, 40, 30)
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
                            enemy_allocation_execute(Africa)
                            greyRectangleAfrica_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this enemy")
                            greyRectangleAfrica_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleAfrica_Enemy = False
                        
                #Enemy status allocation for Middle east
                elif ((540 + enemy_Button_Length) > pos[0] > 540) and ((185 + enemy_Button_Width) > pos[1] > 185):
                    enemy_allocation("the Middle East", MiddleEast)
                    greyRectangleMiddleEast_Enemy = enemy_allocation("the Middle East", MiddleEast)
                elif greyRectangleMiddleEast_Enemy == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        enemy_allocation_confirm(MiddleEast)
                        enemyCapability = enemy_allocation_confirm(MiddleEast)
                        if enemyCapability == True:
                            enemy_allocation_execute(MiddleEast)    
                            greyRectangleMiddleEast_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this enemy")
                            greyRectangleMiddleEast_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleMiddleEast_Enemy = False
                        
                #Enemy status allocation for Asia
                elif ((620 + enemy_Button_Length) > pos[0] > 620) and ((120 + enemy_Button_Width) > pos[1] > 120):
                    enemy_allocation("Asia", Asia)
                    greyRectangleAsia_Enemy = enemy_allocation("Asia", Asia)
                elif greyRectangleAsia_Enemy == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        enemy_allocation_confirm(Asia)
                        enemyCapability = enemy_allocation_confirm(Asia)
                        if enemyCapability == True:
                            enemy_allocation_execute(Asia)    
                            greyRectangleAsia_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this enemy")
                            greyRectangleAsia_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleAsia_Enemy = False
                        
                #Enemy status allocation for Australia
                elif ((770 + enemy_Button_Length) > pos[0] > 770) and ((375 + enemy_Button_Width) > pos[1] > 375):
                    enemy_allocation("Australia", Australia)
                    greyRectangleAustralia_Enemy = enemy_allocation("Australia", Australia)
                elif greyRectangleAustralia_Enemy == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        enemy_allocation_confirm(Australia)
                        enemyCapability = enemy_allocation_confirm(Australia)
                        if enemyCapability == True:
                            enemy_allocation_execute(Australia)    
                            greyRectangleAustralia_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this enemy")
                            greyRectangleAustralia_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleAustralia_Enemy = False
                        
                #Enemy status allocation for South America
                elif ((225 + enemy_Button_Length) > pos[0] > 225) and ((330 + enemy_Button_Width) > pos[1] > 330):
                    enemy_allocation("South America", SouthAmerica)
                    greyRectangleSouthAmerica_Enemy = enemy_allocation("South America", SouthAmerica)
                elif greyRectangleSouthAmerica_Enemy == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        enemy_allocation_confirm(SouthAmerica)
                        enemyCapability = enemy_allocation_confirm(SouthAmerica)
                        if enemyCapability == True:
                            enemy_allocation_execute(SouthAmerica)    
                            greyRectangleSouthAmerica_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this enemy")
                            greyRectangleSouthAmerica_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleSouthAmerica_Enemy = False
                    
                #Enemy status allocation for North america
                elif ((110 + enemy_Button_Length) > pos[0] > 110) and ((165 + enemy_Button_Width) > pos[1] > 165):
                    enemy_allocation("North America", NorthAmerica)
                    greyRectangleNorthAmerica_Enemy = enemy_allocation("North America", NorthAmerica)
                elif greyRectangleNorthAmerica_Enemy == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        enemy_allocation_confirm(NorthAmerica)
                        enemyCapability = enemy_allocation_confirm(NorthAmerica)
                        if enemyCapability == True:
                            enemy_allocation_execute(NorthAmerica)    
                            greyRectangleNorthAmerica_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this enemy")
                            greyRectangleNorthAmerica_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleNorthAmerica_Enemy = False
                    
                #Enemy status allocation for Europe
                elif ((470 + enemy_Button_Length) > pos[0] > 470) and ((125 + enemy_Button_Width) > pos[1] > 125):
                    enemy_allocation("Europe", Europe)
                    greyRectangleEurope_Enemy = enemy_allocation("Europe", Europe)
                elif greyRectangleEurope_Enemy == True:
                    if ((360 + check_Button_Length) > pos[0] > 360) and ((490 + check_Button_Width) > pos[1] > 490):
                        enemy_allocation_confirm(Europe)
                        enemyCapability = enemy_allocation_confirm(Europe)
                        if enemyCapability == True:
                            enemy_allocation_execute(Europe)    
                            greyRectangleEurope_Enemy = False
                            mainGameScreen()
                        elif enemyCapability == False:
                            print("Insufficient funds for this enemy")
                            greyRectangleEurope_Enemy = False
                            mainGameScreen()
                    elif ((520 + x_Button_Length) > pos[0] > 520) and ((490 + x_Button_Width) > pos[1] > 490):
                        mainGameScreen()
                        greyRectangleEurope_Enemy = False
                    
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
