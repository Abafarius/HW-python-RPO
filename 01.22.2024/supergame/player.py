import pygame as pg

class Player:
    size = (0,0)
    position = (0,0)
    color = "green"
    sprites = {}
    current_animation = ""
    frame = 0
    surface: pg.Surface = None

    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color
        self.sprites['right'] = pg.image.load("resources\sprites\Fighter\Turn_2.png")
        self.sprites['left'] = pg.image.load("resources\sprites\Fighter\Turn_1.png")
        self.sprites['up'] = pg.image.load("resources\sprites\Fighter\Move.png")
        self.sprites['down'] = pg.image.load("resources\sprites\Fighter\Move.png")
        self.current_animation = 'right'
        self.surface = pg.Surface(self.size)
        self.surface.set_colorkey((0,0,0))
        self.update()

    def update(self):
        self.surface.fill((0,0,0))
        self.surface.blit(self.sprites[self.current_animation], 
                (0,0), 
                (self.size[0]*self.frame, 0, self.size[0]*(self.frame+1), self.size[1]))
        #        ^^^^^^^^ x1 ^^^^^^^  y1 ^^^^^^^^^ x2 ^^^^^^^^^^  ^^^ y2 ^^^

    def next_frame(self):
        self.frame += 1
        if self.frame > 5:
            self.frame = 0

    def move(self, dx, dy):
        self.position = (self.position[0]+dx, self.position[1]+dy)
        self.next_frame()

    def set_animation(self, new_animation):
        if new_animation in self.sprites and self.current_animation != new_animation:
            self.current_animation = new_animation