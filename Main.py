# Lets keep this strictly for managing which page of the game is being displayed
import pygame
import MainPage as main

window_surface = pygame.display.set_mode((900, 600))

main.mainMenu(window_surface)