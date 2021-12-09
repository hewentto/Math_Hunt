import pygame
import pygame_gui
from pygame.locals import *
from pygame import mixer
import GamePage 
import LevelSelect as ls

def endScreen(window_surface, score):
    pygame.init()

    pygame.mixer.init()

    pygame.mixer.music.load("sound/level_completed.ogg")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    

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

    end_manager = pygame_gui.UIManager((width, height))

    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
    font = "Retro.ttf"

    title = text_format("GAME OVER", font, 90, yellow)

    title_rect = title.get_rect()

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                                text='Play Again',
                                                manager=end_manager)

    yourScore = text_format("Your Score", font, 40, yellow)
    yourScore_rect = yourScore.get_rect()

    highscore = text_format("Highscore", font, 40, yellow)
    highscore_rect = yourScore.get_rect()


                                                

    # Background image
    background_image = pygame.image.load("background.png").convert()

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            end_manager.process_events(event)

            end_manager.update(time_delta)
            if event.type == USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        navigate = pygame.mixer.Sound('sound/navigating_menu.ogg')
                        navigate.play()
                        if event.ui_element == back_button:
                            ls.levelSelect(window_surface)
        window_surface.blit(background_image, [0, 0])
        window_surface.blit(title, (width/2 - (title_rect[2]/2), 50))
        window_surface.blit(yourScore, (275,height/3))
        window_surface.blit(highscore,(475,height/3))
        end_manager.draw_ui(window_surface)

        pygame.display.update()
