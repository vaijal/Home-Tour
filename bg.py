#!/usr/bin/env python
# coding=utf-8
__author__ = 'Vaijayanthi Mala K'
__date__   = '14-Feb-2018'

import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location