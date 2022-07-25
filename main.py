import pygame as p
from game import Game_Menu
from zelda.main import Game

g = Game_Menu()


while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

