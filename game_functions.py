#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:hao

import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    # 响应鼠标和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event,ai_settings, screen, ship, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # 创建一个子弹，加入到bullets
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    # 响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_setting, screen, ship, aliens, bullets):
    # 每次循环都重新描绘屏幕
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def update_buttlets(bullets):
    # 更新子弹的位置并删除消息的子弹
    bullets.update()

    # 删除消息的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建新子弹，并加入编组 bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    # 计算每行可容纳多少个外星人
    available_space_x = ai_settings.screen_width - 1 * alien_width
    number_aliens_x = int(available_space_x / (1 * alien_width))    # 除与 每个占用的宽，就等于 1行 的个数
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人，并将其放入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien_x
    alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    # 创建外星人群
    # 创建一个外星人，并计算每行可容纳的多少个
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算容纳多少行外星人
    available_space_y = (ai_settings.screen_height - (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (1 * alien_height))
    return number_rows

def update_aliens(ai_settings, aliens):
    # j检查外星人的位置是否在边缘，更新外星人的所有位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    # 外星人达到边缘时采取措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    # 将外星人下移
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
