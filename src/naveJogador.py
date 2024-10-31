import pygame
from naveBase import NaveBase

class NaveJogador(NaveBase):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga, aprimoramentos):
        super().__init__(imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga)
        self.aprimoramentos = aprimoramentos
        self.rect = self.imagem.get_rect(topleft=posicao)

    def atirar():
        raise NotImplementedError("Este método deve ser implementado")

    def calcularAprimoramento():
        raise NotImplementedError("Este método deve ser implementado")
