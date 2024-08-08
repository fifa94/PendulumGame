import pygame
import Pendulum
import ButtonsGeneral

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.surface = pygame.Surface((800, 600))
        pygame.display.set_caption('Pendulum Simulation')
        self.clock = pygame.time.Clock()
        self.menu_back_ground = 215, 25, 25
        self.game_back_ground = 255, 255, 255
        #self.pendulum = Pendulum(g=9.81, l=1.0, b=0.1)


    def run(self):

        play_btn = ButtonsGeneral.Button(225, 200, 'Play')
        quit_btn = ButtonsGeneral.Button(225, 300, 'Quit')

        running = True

        menu_state = 'Menu'

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


            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    running = False

            #self.pendulum.update(dt=0.01)
            #self.screen.fill((255, 255, 255))
            # Zde můžeš přidat kód pro vykreslení kyvadla

            pygame.display.flip()
            self.clock.tick(60)
            # Screen update
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()