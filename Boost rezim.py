#knihovny
import sys
import pygame
import time
import random
pygame.init()
#Neznámé
rozliseni_x = 1200
rozliseni_y = 1000

pozice_x = rozliseni_x / 2
pozice_y = rozliseni_y / 2
velikost = 30
rychlost_x = 1
rychlost_y = 1
FPS = 120


hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))



#Program
while True:
    hodiny.tick(FPS)
    for udalost in pygame.event.get():
       
       if udalost.type == pygame.QUIT:
           
           pygame.quit()
           
           sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and pozice_y > 0 :
        pozice_y -= rychlost_y
    if keys[pygame.K_DOWN] and pozice_y < rozliseni_y - velikost :
        pozice_y += rychlost_y
    if keys[pygame.K_LEFT] and pozice_x > 0 :
        pozice_x -= rychlost_x
    if keys[pygame.K_RIGHT] and pozice_x < rozliseni_x - velikost   :
        pozice_x += rychlost_x
    if keys[pygame.K_RSHIFT] == True :
        rychlost_x = 2
        rychlost_y = 2
    if keys[pygame.K_RSHIFT] == False :
        rychlost_x = 1
        rychlost_y = 1
        
        
    if keys[pygame.K_DOWN] and keys[pygame.K_RSHIFT] :
        rychlost_x = 0
    if keys[pygame.K_UP] and keys[pygame.K_RSHIFT] :
        rychlost_x = 0
    if keys[pygame.K_RIGHT] and keys[pygame.K_RSHIFT] :
        rychlost_y = 0
    if keys[pygame.K_LEFT] and keys[pygame.K_RSHIFT] :
        rychlost_y = 0
    okno.fill((252, 255, 255))
    
    

    pygame.draw.rect(okno, (255,0,0), (pozice_x, pozice_y, velikost, velikost))
    pygame.display.update()
