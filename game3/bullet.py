import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,sett,window,ship):
        self.sett=sett
        super(Bullet,self).__init__()
        self.window=window
        self.rect=pygame.Rect(0,0,sett.b_width,sett.b_height)
        self.rect.top=ship.rect_ship.top
        self.rect.centerx=ship.rect_ship.centerx
        self.y=float(self.rect.y)
        self.col=sett.b_col
    def update(self):
        self.y-=self.sett.b_speed
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.window,self.col,self.rect)