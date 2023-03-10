
import pygame
import sys
from pygame.locals import *

# Set up pygame
pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
basicFont = pygame.font.SysFont('Times New Roman', 48)

# set up the text
text = basicFont.render('Hi Jim', True, WHITE, BLUE)
textRect = text.get_rect()

textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

