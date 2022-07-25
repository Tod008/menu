# game setup
SCREEN_W = 1280
SCREEN_H = 720
FPS = 60
TILE_SIZE = 64
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0
}

# ui
BAR_H = 20
HEALTH_BAR_W = 200
ENERGY_BAR_W = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'zelda/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrace colors
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = "#EEEEEE"
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons setup
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': 'zelda/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': 'zelda/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': 'zelda/graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': 'zelda/graphics/weapons/rapier/full.png'}, 
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': 'zelda/graphics/weapons/sai/full.png'}}

# magic setup
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': 'zelda/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': 'zelda/graphics/particles/heal/heal.png'}
}

# enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': 'zelda/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 100, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': 'zelda/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': 'zelda/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': 'zelda/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}