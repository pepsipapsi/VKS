import os
import pygame
import pygame_gui
from settings import *
from pdf_form import *
from pdf_form import pdfRun
import tkinter as tk
from tkinter import *
from tkinter import ttk, Text, Button, LabelFrame, VERTICAL, E, NS, Scrollbar, Tk
from tkinter.filedialog import askopenfilename

pygame.init()
pygame.font.init()
# DISPLAY
window_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT))  # Only displays the curves when 1000
pygame.display.set_caption('Varmekabel Kalkulator og Simulator')


screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(pygame.Color('#123093'))

manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.init()
pygame.display.update()

# VVVVVVVVVV
checkB1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0),
                                                                 (checkW, checkH)),
                                       text='Export',
                                       manager=manager)

# BUTTON PRESSED FUNCTION


def uiButtonPressed():
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == checkB1:  # B1 is just a shorter way of saying Bookmark 1
            writerUpdate(0, pdf_writer, Typebetegnelse, "Hola")
            writerUpdate(0, pdf_writer, CM["To-Leder"], yes)

            pdfRun()
    manager.process_events(event)


def drawBezier(list, t):
    li = list[:]
    while len(li) != 1:
        for pos, x in enumerate(li):
            if x != li[-1]:
                li[pos] = (1-t)*x[0]+t*li[pos+1][0], (1-t)*x[1]+t*li[pos+1][1]
        li.pop()
    return li[0]
# MAIN GAME LOOP


points = [(200, 200), (400, 1500), (800, 200)]
points = [(x[0], 1000-x[1]) for x in points]

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            exit()
        uiButtonPressed()
    t = 0
    while t <= 1:
        point = drawBezier(points, t)
        window_surface.fill((255, 0, 255), (point, (1, 1)))
        t += 0.0001

    manager.update(time_delta)
    manager.draw_ui(window_surface)
    # window_surface.blit(screen, (1000, 0))  # <-- The actual "box"
    pygame.display.update()
