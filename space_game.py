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
    inos = Group()
    controls.create_army(screen, inos)

    while True:
        controls.events(screen, cannon, bullets)
        cannon.update_cannon()
        controls.update(bg_color, screen, cannon, inos, bullets)
        controls.update_bullets(bullets)
        controls.update_inos(inos)

run()

