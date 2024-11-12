import pygame
from objetoJogo import ObjetoJogo


class NaveBase(ObjetoJogo):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga):
        super().__init__(imagem, velocidade, posicao)
        self.pontos_vida = pontos_vida
        self.potencia_tiro = potencia_tiro
        self.tempo_recarga = tempo_recarga
        self.bullets = []


    def obterPotencia():
        raise NotImplementedError("Este método deve ser implementado")
    
    def update():
        pass

