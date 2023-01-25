
import pygame

import random

rozliseni_x = 1200
rozliseni_y = 1000

pozice_x = 0
pozice_y = 0
velikost = 30
rychlost = 1
FPS = 120

hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))

pygame.init()