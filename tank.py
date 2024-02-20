import pygame


class Tank:

    def __init__(self):
        self.position = None
        self.colors = [pygame.Color(255, 255, 255), pygame.Color(255, 0, 0),
                       pygame.Color(0, 255, 0), pygame.Color(0, 0, 255)]
        self.image = pygame.image.load("sprites/sprite1.png").convert_alpha()
        self.zoom = 5
        self.resize_img = pygame.transform.scale(self.image, (self.image.get_width() * self.zoom
                                                              , self.image.get_height() * self.zoom,))
        self.final_image = None

    def choose_tank(self, player, screen):
        colored_image = pygame.Surface(self.resize_img.get_size())
        colored_image.fill(self.colors[player])
        final_image = self.resize_img.copy()
        final_image.blit(colored_image, (0, 0), special_flags=pygame.BLEND_MULT)
        self.final_image = final_image

