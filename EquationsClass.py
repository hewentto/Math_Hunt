# Equations class that will display the equation and save the index of problem also
import pygame
import pygame_gui
from pygame.locals import *

class DisplayProblem:

    x = 375
    y = 550

    def __init__(self, problem, index, screen):
        self.problem = problem
        self.index = index
        self.screen = screen

    def showProblem(self):
        renderText = pygame.font.SysFont("Retro.ttf", 55).render(self.problem, True, (0,0,0))
        self.screen.blit(renderText, (self.x, self.y))
