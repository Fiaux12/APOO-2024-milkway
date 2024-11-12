import pandas as pd
import pygame
from naveInimiga import NaveInimiga
from powerUp import PowerUp


def nivel1(surface):
    nave_inimiga1 = NaveInimiga(
        imagem= "../assets/images/naveEspacial.png",
        velocidade=0.05,
        posicao=[300, 0], 
        pontos_vida=100, 
        potencia_tiro=10, 
        tempo_recarga=1.5,
        tempo_parado=5000
    )

    nave_inimiga2 = NaveInimiga(
        imagem= "../assets/images/naveEspacial.png",
        velocidade=0.05,
        posicao=[400, 0], 
        pontos_vida=100, 
        potencia_tiro=10, 
        tempo_recarga=1.5,
        tempo_parado=5000
    )

    nave_inimiga3 = NaveInimiga(
        imagem= "../assets/images/naveEspacial.png",
        velocidade=0.05,
        posicao=[500, 0], 
        pontos_vida=100, 
        potencia_tiro=10, 
        tempo_recarga=1.5,
        tempo_parado=5000
    )

    nave_inimiga4 = NaveInimiga(
        imagem= "../assets/images/naveEspacial.png",
        velocidade=0.05,
        posicao=[600, 0], 
        pontos_vida=100, 
        potencia_tiro=10, 
        tempo_recarga=1.5,
        tempo_parado=5000
    )

    
    nave_inimiga1.retacionarImagem()
    nave_inimiga2.retacionarImagem()
    nave_inimiga3.retacionarImagem()
    nave_inimiga4.retacionarImagem()

    
    nave_inimigo_redimensionada = pygame.transform.scale(nave_inimiga1.imagem, (70, 70))
    surface.blit(nave_inimigo_redimensionada, nave_inimiga1.posicao)

    nave_inimiga1.rect = nave_inimigo_redimensionada.get_rect(topleft=nave_inimiga1.posicao) 
    nave_inimigo_redimensionada2 = pygame.transform.scale(nave_inimiga2.imagem, (70, 70))
    surface.blit(nave_inimigo_redimensionada2, nave_inimiga2.posicao)
    nave_inimiga2.rect = nave_inimigo_redimensionada2.get_rect(topleft=nave_inimiga2.posicao) 
    nave_inimigo_redimensionada3 = pygame.transform.scale(nave_inimiga3.imagem, (70, 70))
    surface.blit(nave_inimigo_redimensionada3, nave_inimiga3.posicao)
    nave_inimiga3.rect = nave_inimigo_redimensionada3.get_rect(topleft=nave_inimiga3.posicao) 
    nave_inimigo_redimensionada4 = pygame.transform.scale(nave_inimiga4.imagem, (70, 70))
    surface.blit(nave_inimigo_redimensionada4, nave_inimiga4.posicao)
    nave_inimiga4.rect = nave_inimigo_redimensionada4.get_rect(topleft=nave_inimiga4.posicao) 
# CONFLITO AQUI
#     nave_inimigo_redimensionada2 = pygame.transform.scale(nave_inimiga2.imagem, (70, 70))
#     surface.blit(nave_inimigo_redimensionada2, nave_inimiga2.posicao)
#     nave_inimigo_redimensionada3 = pygame.transform.scale(nave_inimiga3.imagem, (70, 70))
#     surface.blit(nave_inimigo_redimensionada3, nave_inimiga3.posicao)
#     nave_inimigo_redimensionada4 = pygame.transform.scale(nave_inimiga4.imagem, (70, 70))
#     surface.blit(nave_inimigo_redimensionada4, nave_inimiga4.posicao)


    naves_inimigas = []
    naves_inimigas.append(nave_inimiga1)
    naves_inimigas.append(nave_inimiga2)
    naves_inimigas.append(nave_inimiga3)
    naves_inimigas.append(nave_inimiga4)
    return naves_inimigas
    
