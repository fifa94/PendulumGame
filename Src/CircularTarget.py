import pygame
import math

class CircularTarget:
    def __init__(self, screen, color, center, radius, width):
        try:
            if isinstance(color, tuple) and len(color) == 3:
                self.color = color
            else:
                raise TypeError(f'Color parameter is in wrong format')
        except Exception as e:
            print(f'An error occurred: {e}')

        try:
            if screen is not None:
                self.screen = screen
            else:
                raise TypeError(f' Screen parameter is empty')
        except Exception as e:
            print(f'An error occurred: {e}')

        try:
            if isinstance(center, tuple) and len(center) == 2:
                self.center = center
            else:
                raise TypeError(f'Center parameter is in wrong format')
        except Exception as e:
            print(f'An error occurred: {e}')

        try:
            if radius > 0:
                self.radius = radius
            else:
                raise TypeError(f'Radius must be greater than 0')
        except Exception as e:
            print(f'An error occurred: {e}')

        try:
            if width > 0:
                self.width = width
                self.target_width = width + 2
            else:
                raise TypeError(f'width must be greater than 0')
        except Exception as e:
            print(f'An error occurred: {e}')

    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius, self.width)
        pygame.draw.arc(self.screen, (0,0,255), (self.center[0]-self.radius, self.center[1]-self.radius, 400, 400), math.radians(85), math.radians(95), self.target_width)

