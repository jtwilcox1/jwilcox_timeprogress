# File created by: JT Wilcox 
# creates pygame
import pygame 
from pygame.sprite import Sprite
from os import path
from math import floor
from settings import *
pygame.init()
# dimensions of the screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
# indicates where the countdown should start from
counter, text = 7, '7'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
# font size and shape
font = pygame.font.SysFont('Arial', 100)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            # subracts one every second
            counter -= 1
            # if the timer is less than 1 it will print this
            text = str(counter).rjust(3) if counter > 0 else 'You lost :('
        if e.type == pygame.QUIT: 
            run = False
    
# color is background and characteristics like color, font, and where to be on the screen
    screen.fill((255, 255, 255))
    def draw_text(text, size, color, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        screen.blit(text_surface, text_rect)
    draw_text("TIMER", 22, BLUE, WIDTH/2, HEIGHT/24)
    # location of the text
    screen.blit(font.render(text, True, (0, 0, 0)), (330, 180))
    pygame.display.flip()
    clock.tick(60)