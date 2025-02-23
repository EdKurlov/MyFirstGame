#!/bin/bash

import pygame
import controls
from cannon import Cannon
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('space defenders')
    bg_color = (0, 0, 0)
    cannon = Cannon(screen)
    bullets = Group()

    while True:
        controls.events(screen, cannon, bullets)
        cannon.update_cannon()
        controls.update(bg_color, screen, cannon, bullets)
        controls.update_bullets(bullets)

run()

