#!bin/bash/
import pygame
import sys
from bullet import Bullet

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

def update(bg_color, screen, cannon, bullets):
    """ Screen refresh"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    cannon.output()
    pygame.display.flip()

def update_bullets(bullets):
    """ Bullet position update"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

 
