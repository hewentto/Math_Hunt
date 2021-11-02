import pygame
import pygame_gui
from pygame.locals import *

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

title = text_format("Score:", font, 50, yellow)

title_rect = title.get_rect()
main_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 540), (100, 50)), text='Main Menu', manager=manager)
duck1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 70), (50, 50)), text='Duck', manager=manager)
duck2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 200), (50, 50)), text='Duck', manager=manager)      
duck3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 100), (50, 50)), text='Duck', manager=manager) 
duck4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 70), (50, 50)), text='Goose', manager=manager)                  

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
    window_surface.blit(title, (650, 10))
    manager.draw_ui(window_surface)

    pygame.display.update()