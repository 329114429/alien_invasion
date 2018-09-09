#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:hao

class Setting():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction  为 1 表示向右， -1 表示向左
        self.fleet_direction = 1

