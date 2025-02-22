#!bin/bash/
import pygame
import sys

def events(cannon):
    """ Processing of events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # right
            if event.key == pygame.K_d:
                cannon.mright = True
            # left
            elif event.key == pygame.K_a:
                cannon.mleft = True
                
        elif event.type == pygame.KEYUP:
            # right
            if event.key == pygame.K_d:
                cannon.mright = False
            # left
            elif event.key == pygame.K_a:
                cannon.mleft = False
    
