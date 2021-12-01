import pygame, sys
import pygame_gui
from pygame.locals import *
import duckClass as Duck
import os
import LevelSelect



# Main Menu
def mainMenu(window_surface):

    # Game Initialization
    pygame.init()

    # Center the Game Application

    # Game Resolution
    screen_width = 900
    screen_height = 600
    pygame.display.set_caption('Math Hunt')
   # Background imgae
    background_image = pygame.image.load("background.png").convert()
    menu_manager = pygame_gui.UIManager((screen_width, screen_height))

    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText


    # Colors
    white=(255, 255, 255)
    black=(0, 0, 0)
    gray=(50, 50, 50)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    yellow=(255, 255, 0)

    # Game Fonts
    font = "Retro.ttf"


    # Game Framerate
    clock = pygame.time.Clock()
    FPS = 30

 

    click = False

    menu = True
    selected = "start"

    mx, my = pygame.mouse.get_pos()

            # Main Menu UI
   
    title=text_format("Math Hunt", font, 90, yellow)
    text_start=text_format("START", font, 75, white)

    title_rect = title.get_rect()
    start_rect = text_start.get_rect()

    # Main Menu Text
    window_surface.blit(background_image, [0,0])
    window_surface.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
    window_surface.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))

    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

    while menu:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected="start"
                elif event.key == pygame.K_DOWN:
                    selected="quit"
                if event.key == pygame.K_RETURN:
                    LevelSelect.levelSelect(window_surface)
#Initialize the Game
