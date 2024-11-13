import pandas as pd
import pygame
from naveInimiga import NaveInimiga
from powerUp import PowerUp
import random
    
def gerar_niveis(surface, quantidade_naves, pontos_vida):
    naves_inimigas = []
    for _ in range(quantidade_naves):
        x_posicao = random.randint(0, 800)  

        nave_inimiga = NaveInimiga(
            imagem = "../assets/images/naveEspacial.png",
            velocidade = 0.3,
            posicao = [x_posicao, -100],  
            pontos_vida = pontos_vida,
            potencia_tiro = 10,
            tempo_recarga = 1.5,
            tempo_parado=pygame.time.get_ticks() + random.randint(50, 1000)  #100000
        )
        naves_inimigas.append(nave_inimiga)
    
    # Desenha as naves na tela
    for nave in naves_inimigas:
        nave.retacionarImagem() 
        nave_imagem_redimensionada = pygame.transform.scale(nave.imagem, (70, 70))
        surface.blit(nave_imagem_redimensionada, nave.posicao)
        nave.rect = nave_imagem_redimensionada.get_rect(topleft=nave.posicao)  # Atualiza a colisão

    return naves_inimigas