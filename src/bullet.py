import pygame
from naveBase import NaveBase
from objetoJogo import ObjetoJogo


class Bullet(ObjetoJogo):
    def __init__(self, velocidade, posicao, potencia_tiro):
        super().__init__( velocidade, posicao, potencia_tiro)
        self.ativo = True 
        self.imagem = '../assets/images/251-2512365_heart-pixel-art-hd-png-download.png'

    def shoot(self):
        self.posicao[1] -= self.velocidade
        if self.posicao[1] < 0:
            self.ativo = False

    def desenhar(self, tela):
        if self.ativo:
            tela.blit(self.imagem, self.posicao)


    def __del__(self):
        self.ativo = False
