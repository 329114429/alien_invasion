#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:hao

import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # 创建一个子弹编组
    bullets = Group()

    # 创建一个外星人组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_buttlets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        pygame.display.flip()
    
run_game()





