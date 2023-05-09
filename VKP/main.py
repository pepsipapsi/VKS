import pygame
import pygame_gui
import sys
from settings import *
from pdf_form import *
from view import View


class Simulation:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Varmekabel Simulator")
        self.clock = pygame.time.Clock()
        self.view = View()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.view.checkB1:
                        self.view.setPdf()
                self.view.manager.process_events(event)
            dt = self.clock.tick() / 1000
            self.view.run(dt)
            self.view.manager.update(dt)
            self.view.manager.draw_ui(self.screen)
            pygame.display.update()


if __name__ == '__main__':
    simulator = Simulation()
    simulator.run()
