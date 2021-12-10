import pygame
import pygame_gui
from pygame.locals import *
from pygame import mixer
import duckClass as Duck
import equations as dic
import EquationsClass as equ
import EndScreen as end
import MainPage as mp

def Game(window_surface, activeDictionary, activeProblem):
    pygame.init()

    pygame.mixer.init()

    pygame.mixer.music.load("sound/gameplay_music.ogg")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

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

    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
    font = "Retro.ttf"

    score = 0

    

    title = text_format("Score:", font, 50, yellow)
    displayProblem = text_format("", font, 90, black)

    title_rect = title.get_rect()
    problem_rect = displayProblem.get_rect()

    main_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 540), (100, 50)), text='Main Menu', manager=game_manager)

    # Background image
    background_image = pygame.image.load("background.png").convert()

    #duck
    addDucks = [Duck.duck(i,activeDictionary[i], window_surface) for i in activeDictionary]
    addProblems = [equ.DisplayProblem(activeProblem[i], i, window_surface) for i in activeProblem]

    clock = pygame.time.Clock()
    is_running = True
    currentProblem = 0

    delThis = False
    
    problemsListLength = 5
    reload = pygame.mixer.Sound('sound/gun_click.ogg')
    while is_running:
        
        renderText = pygame.font.SysFont("Retro.ttf", 50).render(str(score), True, yellow)
        window_surface.blit(background_image, [0, 0])
        window_surface.blit(title, (650, 10))
        window_surface.blit(renderText,(800, 20))

        time_delta = clock.tick(60)/1000.0
        for k in range(len(addDucks)):
            addDucks[k].draw()
            addDucks[k].mover()
            addProblems[currentProblem].showProblem()
        for answer in dic.adddictanswer:
            active_answer = dic.adddictanswer.get(answer)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                shoot = pygame.mixer.Sound('sound/gun_shot.ogg')
                shoot.play()
                mouseLocation = pygame.mouse.get_pos()
                for k in range(len(addDucks)):
                    if mouseLocation[0] >= addDucks[k].x and mouseLocation[0] <= addDucks[k].x+100:
                        if mouseLocation[1] >= addDucks[k].y and mouseLocation[1] <= addDucks[k].y+100:
                            if addDucks[k].index == addProblems[currentProblem].index:
                                print(addDucks[k].index)
                                print(addProblems[k].index)

                                indexToDelete = k
                                delThis = True
                                score += 1

                                

                                print('--------')
                            problemsListLength += -1
                            if problemsListLength == 0:
                                end.endScreen(score, window_surface)
                            currentProblem += 1
                            
                reload.play()
            if event.type == USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    navigate = pygame.mixer.Sound('sound/navigating_menu.ogg')
                    navigate.play()
                    if event.ui_element == main_menu:
                        mp.mainMenu(window_surface)
            if delThis:
                del addDucks[indexToDelete]
                delThis = False

            game_manager.process_events(event)
            game_manager.update(time_delta) 

        window_surface.blit(displayProblem, (300, 500 ))
        game_manager.draw_ui(window_surface)

        pygame.display.update()
