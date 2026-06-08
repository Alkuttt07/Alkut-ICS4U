import pygame
pygame.init()

class interactive(pygame.sprite.Sprite):
    def __init__(self, type, position, image):
        super().__init__()
        self.type = type
        self.image = image
        self.rect = self.image.get_rect(center = position)


bush_img = pygame.image.load('bush.png').convert_alpha()
bush_img = pygame.transform.scale(bush_img, (100, 100))

hole_img = pygame.image.load('hole.png').convert_alpha()
hole_img = pygame.transform.scale(hole_img, (100, 100))