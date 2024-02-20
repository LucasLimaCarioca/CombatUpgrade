import pygame


class Maze:

    def __init__(self):
        self.walls = []
        self.BLACK = pygame.Color(0, 0, 0)
        self.WHITE = pygame.Color(255, 255, 255)

    def wall(self, x, y, zoom, gap):
        left_wall = pygame.Rect(0, gap * zoom, zoom, y - gap * zoom)  # 0 150 5 550
        right_wall = pygame.Rect(x - zoom, gap * zoom, zoom, y - gap * zoom)  # 795 160 5 540
        upper_wall = pygame.Rect(0, gap * zoom, x, zoom)  # 0 160 800 5
        down_wall = pygame.Rect(0, y - zoom, x, zoom)  # 0 795 800 5
        self.walls = [left_wall, right_wall, upper_wall, down_wall]

        file = open("mazes/maze1.txt")
        row = file.readline()
        b = 0
        while row:
            a = 0
            for letter in row:
                if letter == '1':
                    self.walls.append(pygame.Rect(a * 25, (30 * zoom) + b * 25, 25, 25))
                a += 1
            b += 1
            row = file.readline()
        file.close()

    def build(self, screen):

        # draw main walls
        for wall in self.walls:
            pygame.draw.rect(screen, self.WHITE, wall)

    def spawnzones(self, players, x, y, zoom, gap):
        if players == 2:
            spawn1 = (x / 10, zoom * gap - 20 + (y - zoom * gap) / 2)
            spawn2 = (8 * x / 10, zoom * gap - 20 + (y - zoom * gap) / 2)
            spawnzones = [spawn1, spawn2]
            return spawnzones
        else:
            spawn1 = (x / 10, zoom * gap - 20 + (y - zoom * gap) / 5)
            spawn2 = (x / 10, zoom * gap - 20 + 4 * (y - zoom * gap) / 5)
            spawn3 = (8 * x / 10, zoom * gap - 20 + (y - zoom * gap) / 5)
            spawnzones = [spawn1, spawn2, spawn3]
            if players == 4:
                spawn4 = (8 * x / 10, zoom * gap - 20 + 4 * (y - zoom * gap) / 5)
                spawnzones.append(spawn4)
            return spawnzones
