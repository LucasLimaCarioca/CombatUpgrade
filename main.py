import pygame
import maze
import tank

# Screen
zoom = 5
SCREEN_X = 160 * zoom  # 800
SCREEN_Y = 160 * zoom  # 800
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

# Caption
pygame.display.set_caption('Combat')

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

# Initialize walls
maze = maze.Maze()
maze.wall(SCREEN_X, SCREEN_Y, zoom)

# Initialize tank
tank = tank.Tank()

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    screen.fill(BLACK)

    maze.build(screen)
    tank.choose_tank(1, screen)

    pygame.display.flip()
