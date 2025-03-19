import pygame

s_size = 39

class Spritesheet:
    def __init__(self, file):
        self.spritesheet = pygame.image.load(file).convert_alpha()
        
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.fill((0, 0, 0, 0))
        sprite.blit(self.spritesheet, (0, 0), (x + 1, y + 1, width - 2, height - 2))
        return sprite