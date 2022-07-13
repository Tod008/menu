import pygame as p
from game import Game

def main():
    g = Game()
    while True:
        g.update_display()
    
if __name__ == '__main__':
    main()