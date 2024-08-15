import pygame
import Pendulum
import ButtonsGeneral
from pygame.locals import *
import numpy as np
from CircularTarget import CircularTarget


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.surface = pygame.Surface((800, 600))
        pygame.display.set_caption('Pendulum Simulation')
        self.clock = pygame.time.Clock()
        self.menu_background = pygame.image.load('Images/pendulumBackGround.jpg')
        self.game_back_ground = 255, 255, 255
        self.pendulum = Pendulum.Pendulum_nonlinear_model(g=9.81, l=2.0, b=0.8, theta0=np.pi/4, omega0=1.0)
        self.font = pygame.font.Font(None, 36)
        self.circularTarget = CircularTarget(self.screen,
                                             color=(0, 0, 0),
                                             center=(self.screen.get_width() // 2,
                                                     self.screen.get_height() // 2),
                                             radius=self.pendulum.l * 100,
                                             width=2)
        icon = pygame.image.load('Images/pendulum.png')
        pygame.display.set_icon(icon)

    def run(self):
   
        running = True

        menu_state = 'Menu'

        play_btn = ButtonsGeneral.Button(300, 200, 'Play')
        quit_btn = ButtonsGeneral.Button(300, 200 + 70, 'Quit')
        # interni promenne
        external_force = 0
        increment_force = 0
        score = 0
        pendulum_in_region = False
        delay_time = 1000  # Zpoždění 1 sekunda (v milisekundách)
        x_bounds = (382, 418)
        y_bounds = (98, 102)
        # list kde jsou ulozeny pozice pro vykresleni trajektorie
        points = []
        max_points = 50  # Maximální počet bodů v trajektorii

        while running:
            # detekce zmacknuti klavesy
            pressed = pygame.key.get_pressed()

            # main menu screen
            if menu_state == 'Menu':
                self.screen.blit(self.menu_background, (0, 0))

                if play_btn.draw_button(self.screen):
                    menu_state = 'Game'

                if quit_btn.draw_button(self.screen):
                    running = False

            if menu_state == 'Game':
                # navrat do hlavniho menu
                if pressed[pygame.K_SPACE]:
                    menu_state = 'Menu'
                # Naplneni pozadi bilou barvou
                self.screen.fill(self.game_back_ground)
                # update pozice kyvadla
                self.pendulum.update(self.clock.tick(60) / 1000, external_force)
                # ziskavani aktualnich bodu kyvadla
                x, y = self.pendulum.get_positions(self.screen.get_width(), self.screen.get_height())
                # detekce pozice kyvadla v regiony na pricitani bodu
                if ((x >= x_bounds[0]) and (x <= x_bounds[1]) and (y >= y_bounds[0]) and (y <= y_bounds[1])):
                    if not pendulum_in_region:
                        # Pokud hráč vstoupil do regionu poprvé, zaznamená se čas
                        enter_time = pygame.time.get_ticks()
                        pendulum_in_region = True
                    elif pygame.time.get_ticks() - enter_time >= delay_time:
                        # Pokud je hráč v regionu déle než 1 sekundu, přičti skóre
                        score += 1
                        print(f"Skóre: {score}")
                        pendulum_in_region = False  # Znovu nenastaví čas, dokud hráč neopustí a nevstoupí znovu
                else:
                    pendulum_in_region = False
                # zapisovani aktualni pozice kyvadla do pole pro vykresleni trajektori
                points.append((x, y))
                # vyhazovani bodu trajektorie, ktere jiz nejsou potreba
                if len(points) > max_points:
                    points.pop(0)
                # vykresneni kruku, po kterem se kyvadlo pohybuje
                self.circularTarget.draw_circle()
                # Vykreslení kyvadla
                pygame.draw.line(self.screen, (0, 0, 0), (self.screen.get_width() // 2, self.screen.get_height() // 2), (x, y), 4)
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 10)
                # Vykreslení textu
                text_surface_increment_force = self.font.render(f'increment force : {increment_force:.2f}', True, (0, 0, 0))
                text_surface_external_force = self.font.render(f'external force: {external_force:.2f}', True, (0, 0, 0))
                text_surface_score = self.font.render(f'score: {score}', True, (0, 0, 0))
                # samotne vykresleni textu
                self.screen.blit(text_surface_increment_force, (100, 25))
                self.screen.blit(text_surface_external_force, (100, 50))
                self.screen.blit(text_surface_score, (100, 100))
                # Vykresleni trajektorie kyvadla
                for i in range(len(points) - 1):
                    alpha = int(255 * (i / len(points)))  # Výpočet alfa hodnoty
                    color = (255, 0, 0, alpha)
                    pygame.draw.line(self.screen, color, points[i], points[i + 1], 3)

            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
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