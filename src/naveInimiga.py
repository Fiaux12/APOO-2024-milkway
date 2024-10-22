import pygame
from naveBase import NaveBase

class NaveInimiga(NaveBase):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga):
        super().__init__(imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga)

    def atirar():
        raise NotImplementedError("Este método deve ser implementado")

    def destrutor():
        raise NotImplementedError("Este método deve ser implementado")
