import pygame
from pygame.locals import *


class Button(object):

    # Define colors
    text_color = 0, 0, 0
    hover_color = 245, 245, 245
    click_color = 155, 155, 155
    white = 255, 255, 255
    black = 0, 0, 0
    WIDTH = 140
    HEIGHT = 50

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.clicked = False

    def draw_button(self, screen):
        font = pygame.font.SysFont('Constantia', 20)
        action = False
        position = pygame.mouse.get_pos()
        # create pygame rect object
        button_rect = Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

        if button_rect.collidepoint(position) == 1:
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(screen, self.click_color, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                action = True
                self.clicked = False
            else:
                pygame.draw.rect(screen, self.hover_color, button_rect)
        else:
            pygame.draw.rect(screen, self.hover_color, button_rect)
        # White line
        pygame.draw.line(screen, self.white, (self.x, self.y), (self.x + self.WIDTH, self.y), 2)
        pygame.draw.line(screen, self.white, (self.x, self.y), (self.x, self.y + self.HEIGHT), 2)
        # Black line
        pygame.draw.line(screen, self.black, (self.x, self.y + self.HEIGHT), (self.x + self.WIDTH, self.y + self.HEIGHT), 2)
        pygame.draw.line(screen, self.black, (self.x + self.WIDTH, self.y), (self.x + self.WIDTH, self.y + self.HEIGHT), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_color)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.WIDTH / 2) - int(text_len / 2), self.y + 25))

        return action