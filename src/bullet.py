import pygame
from objetoJogo import InterfaceJogo


class Bullet(InterfaceJogo):
    def __init__(self, posicao, imagem, velocidade):
        super().__init__(imagem, velocidade, posicao)
        self.rect = self.imagem.get_rect(center=(self.posicao[0], self.posicao[1]))
        self.rect.x += 44
        self.rect.y -= 42


    def update(self):
        self.rect.y -= self.velocidade

    def draw(self, surface):
        bala_redimensionada = pygame.transform.scale(self.imagem, (30, 80))
        self.rect = bala_redimensionada.get_rect(center=self.rect.center)
        surface.blit(bala_redimensionada, self.rect)
        
