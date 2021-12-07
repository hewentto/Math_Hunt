import pygame
import pygame_gui
from pygame.locals import *
import duckClass as Duck
import equations as dic
from os import path #helps locate items on the computer


def Game(window_surface):
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
    

    background = pygame.Surface((width, height))
    background.fill(pygame.Color('#000000'))

    game_manager = pygame_gui.UIManager((width, height))

    def load_data():
        # load high score
        dir = path.dirname(__file__) #finds where we are running the program
        # path.join combines the folder we are in with the highscore file
        with open(path.join(dir, "highscore.txt"), 'w') as file: # w will write to the file but also create it if it doenst exist
            try:
                highscore = int(file.read()) # add the file and convert to a int
            except: 
                highscore = 0 

    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
    
        return newText
    font = "Retro.ttf"

    title = text_format("Score:", font, 50, yellow)
    problem = text_format("", font, 90, black)

    title_rect = title.get_rect()
    problem_rect = problem.get_rect()

    main_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 540), (100, 50)), text='Main Menu', manager=game_manager) 

    active_problem = ""
    question = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 540), (100, 50)), text=active_problem, manager=game_manager) 
    # Background image
    background_image = pygame.image.load("background.png").convert()

    #duck
    allDucks = [Duck.duck(i,window_surface) for i in dic.adddict]

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        window_surface.blit(background_image, [0, 0])


        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        
            game_manager.process_events(event)

            game_manager.update(time_delta)

        for k in range(len(allDucks)):
            allDucks[k].draw()
            allDucks[k].mover()
        for problem in dic.adddict:
            active_problem = dic.adddict.get(problem)
            
        window_surface.blit(title, (650, 10))
        window_surface.blit(problem, (300, 500 ))
        game_manager.draw_ui(window_surface)

        pygame.display.update()
