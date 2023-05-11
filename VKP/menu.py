import pygame

class Menu():
    def __init__(self, vks, toggle_menu):
        self.vks = vks
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        
    def update(self):
        self.display_surface.blit(Surface(300, 300))