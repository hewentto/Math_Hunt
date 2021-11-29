import pygame
import pygame_gui
from pygame.locals import *
import GamePage as game

def levelSelect(window_surface):
    pygame.init()

    width = 900
    height = 600 

    # Colors
    yellow=(255, 255, 0)

    pygame.display.set_caption('Math Hunt')

    background = pygame.Surface((width, height))
    background.fill(pygame.Color('#000000'))

    level_manager = pygame_gui.UIManager((width, height))

    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
    font = "Retro.ttf"

    title = text_format("Select Level", font, 90, yellow)

    title_rect = title.get_rect()
    addition_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4), (100, 50)), text='Addition', manager=level_manager)
    subtraction_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 80), (100, 50)), text='Subtraction', manager=level_manager)
    multiplication_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 160), (100, 50)), text='Multiplication', manager=level_manager)
    division_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 240), (100, 50)), text='Division', manager=level_manager)

                                                

    # Background image
    background_image = pygame.image.load("background.png").convert()

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == addition_button:
                        print('Addition')
                        game.Game(window_surface)
                    if event.ui_element == subtraction_button:
                        print('Addition')
                    if event.ui_element == multiplication_button:
                        print('Addition')
                    if event.ui_element == division_button:
                        print('Addition')
            

        level_manager.process_events(event)

        level_manager.update(time_delta)

        window_surface.blit(background_image, [0, 0])
        window_surface.blit(title, (width/2 - (title_rect[2]/2), 50))
        level_manager.draw_ui(window_surface)

        pygame.display.update()

