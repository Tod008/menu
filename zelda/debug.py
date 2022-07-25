import pygame as p
p.init()
font = p.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    display_surface = p.display.get_surface()
    debug_surf = font.render(str(info), True, 'white')
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    p.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)