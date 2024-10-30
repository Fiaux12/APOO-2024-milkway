import pygame
from objetoJogo import ObjetoJogo
class powerUp(ObjetoJogo):
    def __init__(self,imagem,posicao,tipo,valor):
        super().__init__(imagem, velocidade=0, posicao=posicao)
        self.tipo = tipo  # Tipo de aprimoramento ('vel' ou 'tiro')
        self.valor = valor  # O valor que será adicionado ao atributo da nave
        self.coletado = False  # Indica se o aprimoramento foi coletado
    def checar_colisao(self, nave):
        if self.posicao==nave.posicao:
            self.aprimorar(nave)
            self.coletado = True
    def aprimorar(self, nave):
        if self.tipo == 'vel':
            nave.velocidade+=self.valor
        elif self.tipo == 'tiro':
            nave.potencia_tiro+=self.valor
        print(f"Aprimoramento aplicado: {self.tipo} aumentado em {self.valor}")
    def draw(self, surface):
        imagem_redimensionada = pygame.transform.scale(self.imagem, (50, 50)) 
        surface.blit(imagem_redimensionada, self.posicao)    