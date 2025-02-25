#!bin/bash/
import pygame
import sys
from bullet import Bullet
from ino import Ino

def events(screen, cannon, bullets):
    """ Processing of events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # right (cannon)
            if event.key == pygame.K_d:
                cannon.mright = True
            # left (cannon)
            elif event.key == pygame.K_a:
                cannon.mleft = True
            # moving of bullets
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, cannon)
                bullets.add(new_bullet)
                
        elif event.type == pygame.KEYUP:
            # right (cannon)
            if event.key == pygame.K_d:
                cannon.mright = False
            # left (cannon)
            elif event.key == pygame.K_a:
                cannon.mleft = False

def update(bg_color, screen, cannon, inos, bullets):
    """ Screen refresh"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    cannon.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """ Bullet position update"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_inos(inos):
    """ Ino position update"""
    inos.update()

def create_army(screen, inos):
    """ Creation of the aliens army"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((700 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 6):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)
        
        
 
