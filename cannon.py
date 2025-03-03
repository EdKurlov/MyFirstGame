#!/bin/bash

import pygame
from pygame.sprite import Sprite

class Cannon(Sprite):

    def __init__(self, screen):
        """ Cannon initialization"""
        super(Cannon, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/cannon.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """ Cannon drawing"""
        self.screen.blit(self.image, self.rect)

    def update_cannon(self):
        """ Cannon position update"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_cannon(self):
        """ Placement of the cannon in the center at the bottom"""
        self.center = self.screen_rect.centerx

