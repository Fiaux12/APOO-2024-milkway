import pygame
from objetoJogo import ObjetoJogo
import time
  
#Criação do bullet com desenho dessa vez

bullet_image = pygame.image.load("../assets/images/asteroideAzul1.png") 

class Bullet:
    def __init__(self, x, y):
        self.image = bullet_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
