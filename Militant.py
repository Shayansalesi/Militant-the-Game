import pygame
from pygame.locals import *
import sys
import os

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,600))
pygame.display.set_caption("Militant, the Game")
background = pygame.Surface(DISPLAYSURF.get_size()).convert()
background.fill((255,255,255))
screen.blit(DISPLAYSURF, (0,0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
