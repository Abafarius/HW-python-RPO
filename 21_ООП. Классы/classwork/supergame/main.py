import pygame as pg
import controls
from player import Player

FPS = 25
bg = pg.image.load('resources/background.jpg')
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1024, 768))
me = Player((95, 159), (512-40, 384-40), "magenta")

gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True
    controls.check()
    screen.blit(bg, (0,0))
    me.update()
    screen.blit(me, me.position)
    pg.display.update()
    clock.tick(FPS)