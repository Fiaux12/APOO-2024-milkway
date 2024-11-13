import pygame
from objetoJogo import ObjetoJogo
import settings 


class PowerUp(ObjetoJogo):
    def __init__(self, imagem, posicao, tipo, valor):
        super().__init__(imagem, velocidade=0, posicao=posicao)
        self.tipo = tipo 
        self.valor = valor  
        self.coletado = False 
        self.rect = self.imagem.get_rect(topleft=posicao)


    def checar_colisao(self, nave):
        if self.rect.colliderect(nave.rect):
            self.coletado = True
            self.aprimorar(nave)
    
    def aprimorar(self, nave):
        if self.tipo == settings.powerUp_velocidade:
            nave.velocidade += self.valor
        elif self.tipo == settings.powerUp_potencia_tiro:
            nave.potencia_tiro += self.valor
    
    def draw(self, surface):
        if not self.coletado:
            imagem_redimensionada = pygame.transform.scale(self.imagem, (50, 50))
            self.rect = imagem_redimensionada.get_rect(topleft=self.posicao) 
            surface.blit(imagem_redimensionada, self.rect.topleft)
    
    def update(self, surface, nave):
        if not self.coletado:
            self.draw(surface)
            self.checar_colisao(nave)
    
    def __del__(self):
        pass