import pygame as p
from zelda.setting import *


class Upgrade():
    def __init__(self, player) -> None:

        # general setup
        self.display_surface = p.display.get_surface()
        self.player = player
        self.attribute_num = len(player.stats)
        self.attribute_name = list(player.stats)
        self.max_value = list(player.max_stats.values())
        self.font = p.font.Font(UI_FONT, UI_FONT_SIZE)

        # item creation
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        # selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        keys = p.key.get_pressed()
        if self.can_move:
            if keys[p.K_RIGHT] and self.selection_index < self.attribute_num - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = p.time.get_ticks()
            elif keys[p.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = p.time.get_ticks()

            if keys[p.K_SPACE] or keys[p.K_UP]:
                self.can_move = False
                self.selection_time = p.time.get_ticks()
                self.item_list[self.selection_index].trigger(self.player)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = p.time.get_ticks()
            if current_time - self.selection_time >= 200:
                self.can_move = True

    def create_items(self):
        self.item_list = []

        for item, item_index in enumerate(range(self.attribute_num)):
            # hor
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_num
            left = (item * increment) + (increment - self.width) // 2
            # vert
            top = self.display_surface.get_size()[1] * 0.1

            # create object
            item = Item(left, top, self.width,
                        self.height, item_index, self.font)
            self.item_list.append(item)

    def display(self):
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):
            # get attributes
            name = self.attribute_name[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_value[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface, self.selection_index,
                         name, value, max_value, cost)


class Item():
    def __init__(self, l, t, w, h, index, font) -> None:
        self.rect = p.Rect(l, t, w, h)
        self.index = index
        self.font = font

    def display_names(self, surface, name, cost, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # title
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(
            midtop=self.rect.midtop + p.math.Vector2(0, 20))

        # cost
        cost_surf = self.font.render(f'{int(cost)}', False, color)
        cost_rect = cost_surf.get_rect(
            midbottom=self.rect.midbottom - p.math.Vector2(0, 20))

        # draw
        surface.blit(title_surf, title_rect)
        surface.blit(cost_surf, cost_rect)

    def display_bar(self, surface, value, max_value, selected):

        # drawing setup
        top = self.rect.midtop + p.math.Vector2(0, 60)
        bottom = self.rect.midbottom - p.math.Vector2(0, 60)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR

        # bar setup
        full_height = bottom[1] - top[1]
        relative_number = (value / max_value) * full_height
        value_rect = p.Rect(top[0] - 15, bottom[1] - relative_number, 30, 10)

        # draw elemnents
        p.draw.line(surface, color, top, bottom, 5)
        p.draw.rect(surface, color, value_rect)

    def trigger(self, player):
        upgrade_attribute = list(player.stats.keys())[self.index]

        if player.exp >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
            player.exp -= player.upgrade_cost[upgrade_attribute]
            player.stats[upgrade_attribute] *= 1.2
            player.upgrade_cost[upgrade_attribute] *= 1.4
        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]

    def display(self, surface, selection_num, name, value, max_value, cost):
        if self.index == selection_num:
            p.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            p.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            p.draw.rect(surface, UI_BG_COLOR, self.rect)
            p.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        self.display_names(surface, name, cost, self.index == selection_num)
        self.display_bar(surface, value, max_value,
                         self.index == selection_num)
