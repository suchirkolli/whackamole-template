import pygame
import random



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        width = 20
        height = 16
        square_size = 32

        mole_rect = mole_image.get_rect(topleft=(0,0))

        def draw_grid():
            for i in range(0, screen.get_width(), square_size):
                pygame.draw.line(screen, (0,0,0), (i,0), (i, screen.get_height()))
            for i in range(0, screen.get_height(), square_size):
                pygame.draw.line(screen, (0,0,0), (0, i), (screen.get_width(), i))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    if mole_rect.collidepoint(mouse_x, mouse_y):

                        rand_x = random.randrange(0, width) * square_size
                        rand_y = random.randrange(0, height) * square_size
                        mole_rect.topleft = (rand_x, rand_y)

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()