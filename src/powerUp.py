import pygame
from objetoJogo import ObjetoJogo
from posicao import Posicao

class PowerUp(ObjetoJogo):
    def __init__(self, imagem, posicao, tipo, valor):
        super().__init__(imagem, velocidade=0, posicao=posicao)
        self.tipo = tipo  # Tipo de aprimoramento ('vel' ou 'tiro')
        self.valor = valor  # O valor que será adicionado ao atributo da nave
        self.coletado = False  # Indica se o aprimoramento foi coletado
    
    def checar_colisao(self, nave):
        if self.rect.colliderect(nave.rect):
            self.coletado = True
            self.aprimorar(nave)
    
    def aprimorar(self, nave):
        if self.tipo == 'vel':
            nave.velocidade += self.valor
        elif self.tipo == 'tiro':
            nave.potencia_tiro += self.valor
        print(f"Aprimoramento aplicado: {self.tipo} aumentado em {self.valor}")
    
    def draw(self, surface):
        if not self.coletado:
            imagem_redimensionada = pygame.transform.scale(self.imagem, (50, 50)) 
            surface.blit(imagem_redimensionada, self.rect.topleft)
    
    def update(self, screen_width, screen_height, surface, nave):
        # Verifica se o power-up não foi coletado,
        if not self.coletado:
            self.draw(surface)
            self.checar_colisao(nave)
    
    def __del__(self):
        print(f"Destruindo o PowerUp do tipo {self.tipo} com valor {self.valor}.")
