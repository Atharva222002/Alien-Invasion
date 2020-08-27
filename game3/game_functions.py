import pygame
import sys
from bullet import Bullet
import bullet
def check_keydown_event(sett,event,window,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.r_motion = True
    elif event.key==pygame.K_SPACE:
        print('hii')
        new_bullet=Bullet(sett,window,ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_LEFT:
        ship.l_motion = True
def check_keyup_event(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.r_motion = False
    elif event.key == pygame.K_LEFT:
        ship.l_motion = False
def events(window,sett,ship,bullets):
    for event in pygame.event.get():
        if event.type==12:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_event(sett,event,window,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_event(ship,event)
def update_screen(sett,window,ship,bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    window.fill(sett.bg)
    ship.blitme()
    pygame.display.flip()