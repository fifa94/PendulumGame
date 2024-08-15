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
        self.pendulum = Pendulum.Pendulum_nonlinear_model(g=9.81, l=2.0, b=0.8, theta0=np.pi/4, omega0=1.0)
        self.font = pygame.font.Font(None, 36)

    def run(self):
   
        running = True

        menu_state = 'Menu'

        play_btn = ButtonsGeneral.Button(300, 200, 'Play')
        quit_btn = ButtonsGeneral.Button(300, 200 + 70, 'Quit')

        external_force = 0
        increment_force = 0
        score = 0

        points = []
        max_points = 50  # Maximální počet bodů v trajektorii

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
                self.pendulum.update(self.clock.tick(60) / 1000, external_force)
                x,y = self.pendulum.get_positions(self.screen.get_width(), self.screen.get_height())
                points.append((x, y))
                if len(points) > max_points:
                    points.pop(0)

                # Ladicí výstup pro kontrolu
                #print(f"Theta: {self.pendulum.theta}, Omega: {self.pendulum.omega}")
                #print(f"Position: x={x}, y={y}")

                # Vykreslení kyvadla
                pygame.draw.line(self.screen, (0, 0, 0), (self.screen.get_width() // 2, self.screen.get_height() // 2), (x, y), 2)
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 10)
                # Vykreslení textu
                text_surface_increment_force  = self.font.render(f'increment force : {increment_force:.2f}', True, (0, 0, 0))
                text_surface_external_force = self.font.render(f'exteranl force: {external_force:.2f}', True, (0, 0, 0))
                text_surface_score = self.font.render(f'score: {external_force}', True, (0, 0, 0))

                self.screen.blit(text_surface_increment_force, (100, 25))
                self.screen.blit(text_surface_external_force, (100, 50))
                self.screen.blit(text_surface_score, (100, 100))

                for i in range(len(points) - 1):
                    alpha = int(255 * (i / len(points)))  # Výpočet alfa hodnoty
                    color = (255, 0, 0, alpha)
                    pygame.draw.line(self.screen, color, points[i], points[i + 1], 2)

            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        menu_state = 'Menu'
                    if event.key == pygame.K_UP:
                        increment_force += 0.1
                    if event.key == pygame.K_DOWN:
                        increment_force -= 0.1
                    if event.key == pygame.K_RIGHT:
                        external_force += increment_force
                    if event.key == pygame.K_LEFT:
                        external_force -= increment_force

            pygame.display.flip()
            self.clock.tick(60)
            # Screen update
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()