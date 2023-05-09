import pygame
import pygame_gui
from settings import *


class VKS(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((32, 64))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(center=pos)

    # TODO: Choose either to make it as a class, or just built in.
