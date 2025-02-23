#!/bin/bash
import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, cannon):
        """ Create a bullet in the cannon position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 240, 19, 7
        self.speed = 1
        self.rect.centerx = cannon.rect.centerx
        self.rect.top = cannon.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """ Moving the bullet up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Drawing the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
