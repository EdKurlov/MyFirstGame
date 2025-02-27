#!/bin/bash

import pygame
import controls
from cannon import Cannon
from pygame.sprite import Group
from stats import Stats

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('space defenders')
    bg_color = (0, 0, 0)
    cannon = Cannon(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()

    while True:
        controls.events(screen, cannon, bullets)
        if stats.run_game:
            cannon.update_cannon()
            controls.update(bg_color, screen, stats, cannon, inos, bullets)
            controls.update_bullets(screen, stats, inos, bullets)
            controls.update_inos(stats, screen, cannon, inos, bullets)

run()
