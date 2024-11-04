import pygame
from naveBase import NaveBase

class NaveJogador(NaveBase):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga, aprimoramentos):
        super().__init__(imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga)
        self.aprimoramentos = aprimoramentos

    def atirar():
        raise NotImplementedError("Este método deve ser implementado")

    def calcularAprimoramento():
        raise NotImplementedError("Este método deve ser implementado")
    
    def update(self, screen_width, screen_height, surface):
        # Verificar teclas pressionadas para movimentar a nave
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.posicao[0] > 0:
            self.posicao[0] -= self.velocidade
            self.rect.topleft=self.posicao
        if teclas[pygame.K_RIGHT] and self.posicao[0] < (screen_width+180) - self.imagem.get_width():
            self.posicao[0] += self.velocidade
            self.rect.topleft=self.posicao
        if teclas[pygame.K_DOWN] and self.posicao[1] < (screen_height+180) - self.imagem.get_height():
            self.posicao[1] += self.velocidade
            self.rect.topleft=self.posicao
        if teclas[pygame.K_UP] and self.posicao[1] > 0:
            self.posicao[1] -= self.velocidade
            self.rect.topleft=self.posicao
        
        nave_jogador_redimensionada = pygame.transform.scale(self.imagem, (100, 100))
        surface.blit(nave_jogador_redimensionada, self.posicao)
