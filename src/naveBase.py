import pygame
from objetoJogo import ObjetoJogo


class NaveBase(ObjetoJogo):
    def __init__(self, imagem, velocidade, posicao, pontos_vida):
        super().__init__(imagem, velocidade, posicao)
        self.pontos_vida = pontos_vida

    def update():
        pass

