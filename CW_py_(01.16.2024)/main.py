import pygame as pg
import controls
import player

FPS = 40

pg.init()

screen = pg.display.set_mode((1024, 768))

me = player.init((192, 192), (512-50, 500), "magenta")

clock = pg.time.Clock()

bg = pg.image.load('resources/backg.png')


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    controls.check()
    screen.blit(bg, (0,10))
    player.update(me)
    screen.blit(me, player.my_position)
    pg.display.update()
    clock.tick(FPS)

    