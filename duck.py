# Duck class to be implemented in game
import pygame
import pygame_gui
import random
import time

font = "Retro.ttf"
yellow = (255, 255, 0)
class duck:
    def __init__(self, equation, screen):

        # this is where the duck right and duck left sprite will be

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
                        (pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 20).size(self.eequation)[1])]
        self.hitbox = pygame.Rect(
            self.x, self.y, self.size[0], self.size[1])

    def draw(self):
        renderText = pygame.font.SysFont(
            'microsoftjhengheimicrosoftjhengheiuibold', 20).render(self.equation, True, self.color)
        self.screen.blit(renderText, (self.x, self.y))
        # pygame.draw.rect(self.screen, (255, 255, 255), self.hitbox, 1)

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
