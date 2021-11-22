import pygame, sys
import pygame_gui
from pygame.locals import *
import duckClass as Duck
import os

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 900
screen_height = 600
screen=pygame.display.set_mode((screen_width, screen_height))

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

# Background imgae
background_image = pygame.image.load("background.png").convert()

click = False

# Main Menu
def mainMenu():

    menu = True
    selected = "start"

    mx, my = pygame.mouse.get_pos()

    while menu:
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
                    if selected == "start":
                        levelSelect()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(background_image, [0,0])
        title=text_format("Math Hunt", font, 90, yellow)
        if selected ==  "start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

def gamePage():
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
    problem = text_format("", font, 90, black)

    title_rect = title.get_rect()
    problem_rect = problem.get_rect()

    main_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 540), (100, 50)), text='Main Menu', manager=manager) 

    # Background image
    background_image = pygame.image.load("background.png").convert()

    #duck
    duck1 = Duck.duck("test",window_surface)
    duck2 = Duck.duck("test",window_surface)
    duck3 = Duck.duck("test",window_surface)
    duck4 = Duck.duck("test",window_surface)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        window_surface.blit(background_image, [0, 0])


        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == KEYDOWN: # if they press escape key to exit
                if event.key == K_ESCAPE:
                    is_running = False

            # if the user presses the main menu button
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == main_menu:
                        mainMenu()

        
        manager.process_events(event)

        manager.update(time_delta)

        
        
        duck1.draw()
        duck1.mover()
        duck2.draw()
        duck2.mover()
        duck3.draw()
        duck3.mover()
        duck4.draw()
        duck4.mover()
        window_surface.blit(title, (650, 10))
        window_surface.blit(problem, (300, 500 ))
        manager.draw_ui(window_surface)

        pygame.display.update()

def levelSelect():
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
    level1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4), (100, 50)), text='Level 1', manager=manager)
    level2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 80), (100, 50)), text='Level 2', manager=manager)
    level3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 160), (100, 50)), text='Level 3', manager=manager)
    level4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 240), (100, 50)), text='Level 4', manager=manager)
    main_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/2 - 50, height/4 + 320), (100, 50)), text='Main Menu', manager=manager)


    # Background image
    background_image = pygame.image.load("background.png").convert()

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                sys.exit()
            if event.type == KEYDOWN: # if they press escape key to exit
                if event.key == K_ESCAPE:
                    is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == level1_button:
                        gamePage()
                    elif event.ui_element == level2_button:
                        gamePage()# will update this when we have more levels
                    elif event.ui_element == level3_button:
                        gamePage()# will update this when we have more levels
                    elif event.ui_element == level4_button:
                        gamePage()# will update this when we have more levels
                    else: 
                        mainMenu()

            

        manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background_image, [0, 0])
        window_surface.blit(title, (width/2 - (title_rect[2]/2), 50))
        manager.draw_ui(window_surface)

        pygame.display.update()

def endScreen():
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

    title = text_format("GAME OVER", font, 90, yellow)

    title_rect = title.get_rect()

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                                text='Play Again',
                                                manager=manager)

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
            if event.type == KEYDOWN: # if they press escape key to exit
                if event.key == K_ESCAPE:
                    is_running = False

        manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background_image, [0, 0])
        window_surface.blit(title, (width/2 - (title_rect[2]/2), 50))
        window_surface.blit(yourScore, (275,height/3))
        window_surface.blit(highscore,(475,height/3))
        manager.draw_ui(window_surface)

        pygame.display.update()

#Initialize the Game
mainMenu()
pygame.quit()
quit()
