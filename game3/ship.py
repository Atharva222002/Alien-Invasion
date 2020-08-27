import pygame
class Ship():
    def __init__(self,screen,sett):
        self.sett=sett
        self.l_motion = False
        self.r_motion = False
        self.screen=screen
        self.img=pygame.image.load('ship.bmp')
        self.rect_screen=screen.get_rect()
        self.rect_ship=self.img.get_rect()
        self.rect_ship.centerx=self.rect_screen.centerx
        self.rect_ship.bottom = self.rect_screen.bottom
        self.center=float(self.rect_ship.centerx)
    def blitme(self):
        self.screen.blit(self.img,self.rect_ship)
    def update(self):
        if self.r_motion and self.rect_ship.right<self.rect_screen.right:
            self.center+=self.sett.ship_speed
        if self.l_motion and self.rect_ship.left>0:
            self.center-=self.sett.ship_speed
        self.rect_ship.centerx=self.center