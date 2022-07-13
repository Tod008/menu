import pygame as p

class Game():
    def __init__(self):
        p.init()
        self.GAME_W, self.GAME_H = 900, 500
        self.SCREEN_W, self.SCREEN_H = 900, 500
        self.screen = p.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.display = p.Surface((self.GAME_W, self.GAME_H))
        self.BLACK = (0, 0, 0)
    
    def update_display(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
        self.screen.fill(self.BLACK)
        p.display.update()