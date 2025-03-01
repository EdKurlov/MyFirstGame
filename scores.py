#!/bin/bash
import pygame.font
from cannon import Cannon
from pygame.sprite import Group

class Scores():
    """ Output of game information"""
    def __init__(self, screen, stats):
        """ Initializing the scoring of the game"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (240, 19, 7)
        self.font = pygame.font.SysFont(None, 30)
        self.image_score()
        self.image_high_score()
        self.image_cannons()

    def image_score(self):
        """ Converting game score text to graphic image"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """ Showing the game's score record on the screen"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_cannons(self):
        """ Number of lives"""
        self.cannons = Group()
        for cannon_number in range(self.stats.cannons_left):
            cannon = Cannon(self.screen)
            cannon.rect.x = 15 + cannon_number * cannon.rect.width
            cannon.rect.y = 20
            self.cannons.add(cannon)

    def show_score(self):
        """ Displaying the game score on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.cannons.draw(self.screen)
        
        
