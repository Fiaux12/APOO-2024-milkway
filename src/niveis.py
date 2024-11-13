import pygame
from naveInimiga import NaveInimiga
import settings 
import random
    
#Gera uma nova lista de naves em posições aleatorias 
def gerar_niveis(surface):
    naves_inimigas = []
    for _ in range(settings.qtd_inimigas):
        x_posicao = random.randint(0, 800)  

        nave_inimiga = NaveInimiga(
            imagem = "../assets/images/naveEspacial.png",
            velocidade = settings.velocidade_inimigo,
            posicao = [x_posicao, settings.posicao_inicial_y],  
            pontos_vida = settings.pontos_vida_inimigo,
            tempo_parado=pygame.time.get_ticks() + random.randint(50, settings.tempo_geracao)  
        )
        naves_inimigas.append(nave_inimiga)
    
    for nave in naves_inimigas:
        nave.retacionarImagem() 
        nave_imagem_redimensionada = pygame.transform.scale(nave.imagem, (70, 70))
        surface.blit(nave_imagem_redimensionada, nave.posicao)
        nave.rect = nave_imagem_redimensionada.get_rect(topleft=nave.posicao) 

    return naves_inimigas