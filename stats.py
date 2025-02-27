#!/bin/bash
class Stats():
    """ Tracking statistics"""

    def __init__(self):
        """ Statistics initialization"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """ Statistics that change during the game"""
        self.cannons_left = 2
        self.score = 0
