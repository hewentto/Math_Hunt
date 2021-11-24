# Duck class to be implemented in game
import pygame
import pygame_gui
import random
import time

font = "Retro.ttf"
yellow = (255, 255, 0)
class duck:

    duckPairs = [('\brownleft.png','/brownright.png'),('\whiteleft.png','\whiteright.png'),()))]
    def __init__(self, equation, screen):

        # this is where the duck right and duck left sprite will be
        self.sprite = pygame.image.load('images\yellowleft.png')
        self.equation = equation
        self.screen = screen
        # creates a random position for x and y within the screen range for the object
        self.x = random.randrange(20, 800 - 20, 1)
        self.y = random.randrange(20, 600 - 20, 1)
        # creats random direction and speed for the object
        self.vx = random.randrange(-3, 3, 1)
        if self.vx != 0:
            self.vy = random.randrange(-3, 3, 1)
        else:
            self.vy = random.randrange(1, 3, 1)
        self.color = yellow
        self.size = [(pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 20).size(self.equation)[0]),
                        (pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 20).size(self.equation)[1])]
        self.hitbox = pygame.Rect(
            self.x, self.y, self.size[0], self.size[1])

    

    def draw(self):
        renderText = pygame.font.SysFont(font, 20).render(self.equation, True, self.color)
        self.screen.blit(self.sprite, (self.x,self.y +5))
        self.screen.blit(renderText, (self.x, self.y))

        #pygame.draw.rect(self.screen, (255, 255, 255), self.hitbox, 1)

    def mover(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.size[0] >= 800:
            self.vx *= -1
            self.x = 800 - self.size[0]
        if self.x <= 0:
            self.vx *= -1
            self.x = 0
        if self.y + self.size[1] >= 600:
            self.vy *= -1
            self.y = 600 - self.size[1]
        if self.y <= 0:
            self.vy *= -1
            self.y = 0

        # Update the hit box location
        self.hitbox.update(self.x, self.y, self.size[0], self.size[1])

    adddict = {'1': '6 + 6', '1': '12',
                '2': '4 + 4', '2': '8',
                '3': '10 + 13', '3': '23',
                '4': '20 + 70', '4': '90',
                '5': '81 + 3','5': '84',
                '6': '41 + 40', '6': '81',
                '7': '66 + 30', '7': '96',
                '8': '11 + 10', '8': '21',
                '9': '15 + 13', '9': '28',
                '10': '16 + 22', '10': '38',
                '11': '70 + 23', '11': '93',
                '12': '88 + 11 ', '12': '99',
                '13': '35 + 10 ', '13': '45',
                '14': '34 + 35', '14': '69',
                '15': '32 + 33', '15': '65',
                '16': '20 + 8', '16': '28',
                '17': '11 + 3', '17': '14',
                '18': '15 + 5', '18': '20',
                '19': '31 + 8', '19': '39',
                '20': '44 + 11', '20': '55'}
    subdict = {'1': '13 - 10', '1': '3',
                '2': '70 - 20', '2': '50',
                '3': '81 - 3', '3': '78',
                '4': '41 - 40', '4': '1',
                '5': '66 - 30', '5': '36',
                '6': '11 - 10', '6': '1',
                '7': '15 - 13', '7': '2',
                '8': '22 - 16', '8': '6',
                '9': '70 - 23', '9': '47',
                '10': '88 - 11', '10': '77',
                '11': '35 - 10', '11': '25',
                '12': '35 - 34', '12': '1',
                '13': '33 - 32', '13': '1',
                '14': '20 - 8', '14': '12',
                '15': '11 - 3', '15': '8',
                '16': '15 - 5', '16': '10',
                '17': '31 - 8', '17': '23',
                '18': '44 - 11', '18': '33',
                '19': '15 - 7', '19': '8',
                '20': '69 - 12', '20': '57'}
    multdict = {'1': '10 * 13', '1': '130',
                '2': '5 * 6', '2': '30',
                '3': '7 * 3', '3': '21',
                '4': '6 * 4', '4': '24',
                '5': '11 * 12', '5': '132',
                '6': '2 * 5', '6': '10',
                '7': '15 * 4', '7': '60',
                '8': '3 * 2', '8': '6',
                '9': '7 * 7', '9': '49',
                '10': '9 * 7', '10': '63',
                '11': '4 * 3', '11': '12',
                '12': '1 * 3', '12': '3',
                '13': '2 * 6', '13': '12',
                '14': '7 * 8', '14': '56',
                '15': '11 * 3', '15': '33',
                '16': '15 * 5', '16': '75',
                '17': '3 * 8', '17': '24',
                '18': '4 * 11', '18': '44',
                '19': '4 * 1', '19': '4',
                '20': '3 * 5', '20': '15'}
    divdict = {'1': '10 / 2', '1': '5',
                '2': '40 / 5', '2': '8',
                '3': '4 / 4', '3': '1',
                '4': '6 / 3', '4': '2',
                '5': '49 / 7', '5': '7',
                '6': '24 / 6', '6': '4',
                '7': '77 / 7', '7': '11',
                '8': '30 / 6', '8': '5',
                '9': '27 / 9', '9': '3',
                '10': '32 / 8', '10': '4',
                '11': '56 / 7', '11': '8',
                '12': '8 / 2', '12': '4',
                '13': '18 / 2', '13': '9',
                '14': '28 / 4', '14': '7',
                '15': '16 / 2', '15': '8',
                '16': '4 / 2', '16': '2',
                '17': '7 / 7', '17': '1',
                '18': '8 / 0', '18': '0',
                '19': '18 / 3', '19': '6',
                '20': '144 / 12', '20': '12'}