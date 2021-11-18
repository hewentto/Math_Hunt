import pygame
import pygame_gui
from pygame.locals import *

class LevlSelect:
    pygame.init()

    width = 900
    height = 600 

    # Colors
    white=(255, 255, 255)
    black=(0, 0, 0)
    gray=(50, 50, 50)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    yellow=(255, 255, 0)

    pygame.display.set_caption('Math Hunt')
    window_surface = pygame.display.set_mode((width, height))

    background = pygame.Surface((width, height))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((width, height))

    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
    font = "Retro.ttf"

    title = text_format("Select Level", font, 90, yellow)

    title_rect = title.get_rect()
    level1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4), (100, 50)), text='Level1', manager=manager)
    level2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 80), (100, 50)), text='Level2', manager=manager)
    level3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 160), (100, 50)), text='Level3', manager=manager)
    level4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 240), (100, 50)), text='Level4', manager=manager)

                                                

    # Background image
    background_image = pygame.image.load("background.png").convert()

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background_image, [0, 0])
        window_surface.blit(title, (width/2 - (title_rect[2]/2), 50))
        manager.draw_ui(window_surface)

        pygame.display.update()
