import pygame as pg
class Fireball:
    speed = (0, 0)
    position = (0, 0)
    size = (150, 151)
    frame = 0
    parent: pg.Surface = None
    surface: pg.Surface = None


    def __init__(self, parent, position, speed):
        self.parent = parent
        self.position = position
        self.speed = speed
        self.sprite = pg.image.load('')
        self.surface = pg.Surface(self.size)
        self.surface.set_colorkey((0,0,0))
        self.update()


    def move(self):
        dx, dy = self.speed
        if dx or dy:
            self.position = (self.position[0]+dx, self.position[1]+dy)
            self.next_frame()


    def update(self):
        self.surface.fill((0,0,0))
        self.surface.blit(self.sprites[self.current_animation], 
                (0,0), 
                (self.size[0]*self.frame, 0, self.size[0]*(self.frame+1), self.size[1]))
        #        ^^^^^^^^ x1 ^^^^^^^  y1 ^^^^^^^^^ x2 ^^^^^^^^^^  ^^^ y2 ^^^


    def next_frame(self):
        self.frame += 1
        if self.frame > 7:
            self.frame = 5