#from pickle import TRUE
import 8-BIT WONDER.TFF
import pygame as p


class Game():
    def __init__(self):
        p.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = p.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = p.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TFF'
        #self.font_name = p.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20,
                           self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0, 0))
            p.display.update()
            self.reset_keys()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running, self.playing = False, False
            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    self.START_KEY = True
                if event.key == p.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == p.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == p.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = p.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
