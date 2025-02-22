#!/bin/bash

import pygame
import sys
from cannon import Cannon

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption('space defenders')
    bg_color = (0, 0, 0)
    cannon = Cannon(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        cannon.output()
        pygame.display.flip()

run()

