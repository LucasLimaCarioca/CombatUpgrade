import pygame
import maze
import tank

# Screen
zoom = 5
gap = 30
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
maze.wall(SCREEN_X, SCREEN_Y, zoom, gap)

# Get Spawnzones
players = 2
spawnzones = maze.spawnzones(players, SCREEN_X, SCREEN_Y, zoom, gap)

# Initialize tank
speed = 3
tanks = []
colors = [pygame.Color(255, 255, 255), pygame.Color(255, 0, 0),
          pygame.Color(0, 255, 0), pygame.Color(0, 0, 255)]
for i in range(players):
    tanks.append(tank.Tank(zoom, spawnzones[i], speed, colors[i]))

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    screen.fill(BLACK)

    maze.build(screen)
    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_a]:
        tanks[1].action(screen, 1)
    elif keypressed[pygame.K_d]:
        tanks[1].action(screen, 2)
    elif keypressed[pygame.K_w]:
        tanks[1].action(screen, 3)
    screen.blit(tanks[0].final_image, (tanks[0].rect.x, tanks[0].rect.y))
    pygame.display.flip()
