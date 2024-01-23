import pygame as pg
import player

def check():
    keys = pg.key.get_pressed()
    # if pg.K_UP in keys:
    if keys[pg.K_UP]:
        player.move(0, -10)    
    if keys[pg.K_DOWN]:
        player.move(0, 10)    
    if keys[pg.K_LEFT]:
        player.move(-10, 0)    
    if keys[pg.K_RIGHT]:
        player.move(10, 0)    