import pygame as pg
import player

def check(player):
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        player.set_animation('up')
        player.move(0, -10)
    if keys[pg.K_DOWN]:
        player.set_animation('down')
        player.move(0, 10)
    if keys[pg.K_LEFT]:
        player.set_animation('left')
        player.move(-10, 0)
    if keys[pg.K_RIGHT]:
        player.set_animation('right')
        player.move(10, 0)



