from pip import main
import pygame as p
from zelda.setting import *
from zelda.level import Level
from zelda.debug import debug

class Game():
    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((SCREEN_W, SCREEN_H))
        p.display.set_caption('Zelda')
        self.clock = p.time.Clock()
        self.level = Level()

        # sound
        main_sound = p.mixer.Sound('zelda/audio/main.ogg')
        main_sound.set_volume(0.1)
        main_sound.play(loops = -1)
    
    def run(self):
        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                if event.type == p.KEYDOWN:
                    if event.key == p.K_m:
                        self.level.toggle_menu()
                    
            self.screen.fill(WATER_COLOR)
            self.level.run()
            debug(self.clock.get_fps())
            p.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    g = Game()
    g.run()
