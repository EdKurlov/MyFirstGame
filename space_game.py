#!/bin/bash

import pygame
import controls
from cannon import Cannon

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('space defenders')
    bg_color = (0, 0, 0)
    cannon = Cannon(screen)

    while True:
        controls.events(cannon)
        cannon.update_cannon()
        screen.fill(bg_color)
        cannon.output()
        pygame.display.flip()

run()
