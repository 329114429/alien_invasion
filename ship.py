#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:hao
import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx    # centerx 坐标中间的意思
        self.rect.bottom = self.screen_rect.bottom

        # 飞船中储存的最小值
        self.center = float(self.rect.centerx)

        # 移动标志，一开始为 假， 就不移动
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据 self.center 更新 rect 对象
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
