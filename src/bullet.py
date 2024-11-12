import pygame
from objetoJogo import ObjetoJogo


class Bullet(ObjetoJogo):
    def __init__(self, posicao, potencia_tiro, imagem, velocidade):
        super().__init__(imagem, velocidade, posicao)
        self.rect = self.imagem.get_rect(center=(self.posicao[0], self.posicao[1]))
        self.speed = velocidade  
        self.rect.x += 44
        self.rect.y -= 42


    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.imagem, self.rect)
