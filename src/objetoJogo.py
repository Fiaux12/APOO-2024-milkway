import pygame
from posicao import Posicao
from abc import ABC, abstractmethod

class InterfaceJogo(ABC):
    def __init__(self, image, velocidade, posicao: Posicao):
        self.imagem = pygame.image.load(image)

        self.velocidade = velocidade
        self.posicao = posicao
        self.rect = self.imagem.get_rect(topleft=posicao)

    @abstractmethod
    def update():
        pass

        