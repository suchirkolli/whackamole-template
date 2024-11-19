import pygame
import random

def main():
    try:
        pygame.init()
        SCREEN_WIDTH, SCREEN_HEIGHT = 640, 512
        GRID_SIZE = 32  
        GREEN = (200, 240, 150)
        BLACK = (0,0,0)
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_pos = (0,0)
        def draw_grid():
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):  # Vertical lines
                pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):  # Horizontal lines
                pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))
        def draw_mole(position):
            x, y = position
            screen.blit(mole_image, mole_image.get_rect(topleft=(x * GRID_SIZE, y * GRID_SIZE)))
        def is_mole_clicked(position, mouse_pos):
            x, y = position
            mole_rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            return mole_rect.collidepoint(mouse_pos)

        def move_mole():
            new_x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1)
            new_y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
            return (new_x, new_y)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
