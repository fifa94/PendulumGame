import pygame
import Pendulum
import ButtonsGeneral
from pygame.locals import *
import numpy as np

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.surface = pygame.Surface((800, 600))
        pygame.display.set_caption('Pendulum Simulation')
        self.clock = pygame.time.Clock()
        self.menu_back_ground = 215, 25, 25
        self.game_back_ground = 255, 255, 255
        self.pendulum = Pendulum.Pendulum_nonlinear_model(g=9.81, l=1.0, b=0.8, theta0=np.pi, omega0=1.0)

    def run(self):
   
        running = True

        menu_state = 'Menu'

        play_btn = ButtonsGeneral.Button(300, 200, 'Play')
        quit_btn = ButtonsGeneral.Button(300, 200 + 70, 'Quit')

        while running:

            # main menu screen
            if menu_state == 'Menu':
                self.screen.fill(self.menu_back_ground)

                pressed = pygame.key.get_pressed()

                if play_btn.draw_button(self.screen) or pressed[pygame.K_SPACE]:
                    menu_state = 'Game'

                if quit_btn.draw_button(self.screen):
                    running = False

            if menu_state == 'Game':
                self.screen.fill(self.game_back_ground)
                self.pendulum.update(self.clock.tick(60) / 1000)
                x,y = self.pendulum.get_positions(self.screen.get_width(), self.screen.get_height())
                  # Ladicí výstup pro kontrolu
                print(f"Theta: {self.pendulum.theta}, Omega: {self.pendulum.omega}")
                print(f"Position: x={x}, y={y}")

                      # Vykreslení kyvadla
                pygame.draw.line(self.screen, (0, 0, 0), (self.screen.get_width() // 2, self.screen.get_height() // 2), (x, y), 2)
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 10)

            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(60)
            # Screen update
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()