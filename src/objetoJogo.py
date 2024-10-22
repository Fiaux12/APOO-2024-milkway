import pygame
from posicao import Posicao

class ObjetoJogo:
    def __init__(self, image, velocidade, posicao: Posicao):
        self.imagem = pygame.image.load(image)

        self.velocidade = velocidade
        self.posicao = posicao

    def update():
        raise NotImplementedError("Este método deve ser implementado")

        