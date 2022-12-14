import random
import os

import pygame as pg

class Lindasalien(pg.sprite.Sprite):

    images = []

    def __init__(self):
        pg.sprite.Sprite__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1,1)) * Lindasalien.speed
        self.frame = 0
        if self.facine < 0:
            self.rect.right = SCREENRECT.right


    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom +1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame +1
        self.image = self.images[self.frame // self.animcycle % 3]
