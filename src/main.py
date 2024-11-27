import pygame as pg
import sys
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Shui")
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        pass
    
    def new(self):
        #initialisation all variables and setup game
        self.all_sprites = pg.sprite.Group()

    def run(self):
        # game loop - set self.playing = False to end game
        self.playing = True
        while self.playing:
                self.dt = self.clock.tick(FPS) / 1000
                self.events()
                self.update()
                self.draw()
    
    def quit(self):
         pg.quit()
         sys.exit()
    
    def update(self):
         # update portion of the game loop
         self.all_sprites.update()
    
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    def events(self):
         
