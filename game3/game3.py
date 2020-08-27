import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
pygame.init()
def run():
    sett=Settings()
    window = pygame.display.set_mode((sett.winx,sett.winy))
    pygame.display.set_caption('Alien Invasion')
    ship=Ship(window,sett)
    bullets=Group()
    print(type(bullets))
    while True:
        gf.events(window,sett,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(sett,window,ship,bullets)
run()