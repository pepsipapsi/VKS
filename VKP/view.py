import pygame
import pygame_gui
from settings import *
from pdf_form import *
from pdf_form import pdfRun
from vks import VKS


class View:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.checkB1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (checkW, checkH)),
                                                    text='Export',
                                                    manager=self.manager)
        self.setup()

    def setup(self):
        self.vk_simulation = VKS((600, 400), self.all_sprites)

    def setPdf(self):
        writerUpdate(0, pdf_writer, Typebetegnelse, "Test123")
        writerUpdate(0, pdf_writer, CM["To-Leder"], yes)
        pdfRun()

    def run(self, dt):
        self.display_surface.fill("red")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)