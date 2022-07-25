import pygame as p

class Weapon(p.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]

        # graphics
        full_path = f'zelda/graphics/weapons/{player.weapon}/{direction}.png'
        self.image = p.image.load(full_path).convert_alpha()

        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + p.math.Vector2((0, 16)))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + p.math.Vector2((0, 16)))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + p.math.Vector2((-10, 0)))
        elif direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + p.math.Vector2((-10, 0)))
        else:
            self.rect = self.image.get_rect(center = player.rect.center)