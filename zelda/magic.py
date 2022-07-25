from pickletools import read_unicodestring1
import pygame as p
from zelda.setting import *
from random import randint

class Magic():
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': p.mixer.Sound('zelda/audio/heal.wav'),
            'flame': p.mixer.Sound('zelda/audio/Fire.wav')
        }
        self.sounds['heal'].set_volume(0.1)
        self.sounds['flame'].set_volume(0.1)

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['flame'].play()

            if player.status.split('_')[0] == 'right':
                direction = p.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = p.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = p.math.Vector2(0, -1)
            else:
                direction = p.math.Vector2(0, 1)
            
            for i in range(1, 6):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILE_SIZE
                    x = player.rect.centerx + offset_x + randint(-TILE_SIZE // 3, TILE_SIZE // 3)
                    y = player.rect.centery + randint(-TILE_SIZE // 3, TILE_SIZE // 3)
                    self.animation_player.create_particles('flame', (x, y), groups)
                else: # vertical
                    offset_y = (direction.y * i) * TILE_SIZE
                    x = player.rect.centerx + randint(-TILE_SIZE // 3, TILE_SIZE // 3)
                    y = player.rect.centery + offset_y + randint(-TILE_SIZE // 3, TILE_SIZE // 3)
                    self.animation_player.create_particles('flame', (x, y), groups)

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            self.sounds['heal'].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center + p.math.Vector2(0, -60), groups)