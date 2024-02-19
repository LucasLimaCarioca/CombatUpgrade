import pygame


class Tank:

    def __init__(self):
        self.x = None
        self.y = None
        self.colors = [pygame.Color(255, 255, 255), pygame.Color(255, 0, 0),
                       pygame.Color(0, 255, 0), pygame.Color(0, 0, 255)]
        self.image = pygame.image.load("sprites/sprite1.png")
        self.rect = self.image.get_rect()

    def choose_tank(self, player, screen):
        colored_image = pygame.Surface([25, 25])
        colored_image.fill(self.colors[player])
        screen.blit(self.image, self.image.get_rect(center = screen.get_rect().center))
        pygame.display.flip()
