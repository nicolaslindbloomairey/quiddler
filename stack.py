import pygame
from card import Card

class Stack(pygame.sprite.Sprite):
    def __init__(self, card):
        pygame.sprite.Sprite.__init__(self)

        self.cards = [] # list of cards
        

