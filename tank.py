import pygame
import math


def sprite(images, which, zoom, color):
    image = images[which]
    resize_img = pygame.transform.scale(image, (image.get_width() * zoom, image.get_height() * zoom))
    colored_image = pygame.Surface(resize_img.get_size())
    colored_image.fill(color)
    final_img = resize_img.copy()
    final_img.blit(colored_image, (0, 0), special_flags=pygame.BLEND_MULT)
    return final_img


class Tank:

    def __init__(self, zoom, spawn, speed, color):
        self.position = spawn
        self.color = color
        self.images = []
        for i in range(5):
            self.images.append(pygame.image.load("sprites/sprite" + str(i + 1) + ".png").convert_alpha())

        self.final_image = sprite(self.images,0, zoom, color)
        self.rect = self.final_image.get_rect()
        self.rect.update(spawn, (self.rect.x, self.rect.y))
        self.angle = 0
        self.speed = speed

    def action(self, screen, command):
        if command == 1:
            self.angle -= 2
        elif command == 2:
            self.angle += 2
        elif command == 3:
            self.rect.move_ip(math.cos(math.radians(self.angle)) * self.speed,
                              math.sin(math.radians(self.angle)) * self.speed)

        if self.angle == 360:
            self.angle = 0

        screen.blit(self.final_image, (self.rect.x, self.rect.y))
