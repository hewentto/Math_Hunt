# Duck class to be implemented in game
import random
import time

import pygame
import pygame_gui

font = "Retro.ttf"
yellow = (0, 0, 0)


class duck:
    duckPairs = [('images/brownleft.png','images/brownright.png'),('images/whiteleft.png','images/whiteright.png'),('images/yellowleft.png','images/yellowright.png')]
    width = 900
    height = 425 
    
    def __init__(self, equation, index, screen):
        self.index = index
        self.equation = equation
        self.screen = screen
        # creates a random position for x and y within the screen range for the object
        self.x = random.randrange(20, duck.width - 20, 1)
        self.y = random.randrange(20, duck.height - 20, 1)
        self.vx = random.randrange(-3, 3, 1)
        self.vy = random.randrange(-3, 3, 1)
        if self.vx == 0:
            self.vx = random.randrange(-3, 3, 1)
        elif self.vy == 0:
            self.vy = random.randrange(-3, 3, 1)
        # creats random direction and speed for the object
        
        # this is where the duck right and duck left sprite will be
        
        self.duckColor = random.choice(duck.duckPairs)
        self.direction = self.chooseDirection()
        self.sprite = pygame.image.load(self.direction)
        
        

        self.color = yellow
        self.size = [(pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 20).size(self.equation)[0]),
                        (pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 20).size(self.equation)[1])]
        self.hitbox = pygame.Rect(
            self.x, self.y, self.x + 50, self.y + 50)

    def chooseDirection(self):
        if self.vx < 0:
            return self.duckColor[0]
        else:
            return self.duckColor[1]

    def draw(self):
        renderText = pygame.font.SysFont(font, 20).render(self.equation, True, self.color)
        self.screen.blit(self.sprite, (self.x,self.y))
        self.screen.blit(renderText, (self.x + 38, self.y + 75))

        #pygame.draw.rect(self.screen, (255, 255, 255), self.hitbox, 1)

    def mover(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.size[0] >= duck.width:
            self.vx *= -1
            self.x = 800 - self.size[0]
            self.sprite = pygame.image.load(self.duckColor[0])
        if self.x <= 0:
            self.vx *= -1
            self.x = 0
            self.sprite = pygame.image.load(self.duckColor[1])
        if self.y + self.size[1] >= duck.height:
            self.vy *= -1
            self.y = duck.height - self.size[1]
        if self.y <= 0:
            self.vy *= -1
            self.y = 0

        # Update the hit box location
        self.hitbox.update(self.x, self.y, self.size[0], self.size[1])


