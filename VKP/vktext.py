import pygame
from settings import *

class VKText(pygame.sprite.Sprite):
    def __init__(self, text, size, color, font=None, **kwargs):
        super(VKText, self).__init__()
        self.color = color
        self.font = pygame.font.Font(font, size)
        self.kwargs = kwargs
        self.set(text)

    def set(self, text):
        self.image = self.font.render(str(text), 1, self.color)
        self.rect = self.image.get_rect(**self.kwargs)