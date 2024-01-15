import pygame as pg
pg.init()
screen = pg.display.set_mode((800,600))

gameover = False
while gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True