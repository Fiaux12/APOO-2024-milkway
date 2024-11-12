import pygame
from usuario import Usuario
from naveJogador import NaveJogador
import niveis 
import manipularArquivos 
import telas 
import time
from bullet import Bullet
from powerUp import PowerUp


pygame.init()

# Estados do jogo
TELA_INICIAL = "tela_inicial"
MENU = "menu"
NOVO_JOGO = "novo_jogo"
CONTINUAR = "continuar"
MELHORES_JOGADORES = "melhores_jogadores"
estado = TELA_INICIAL
settings = manipularArquivos.ler_configuracoes()

# Cria tela do Pygame
screen_width = settings["Tela"]["screen_width"]
screen_height = settings["Tela"]["screen_height"]
surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MilkWay')
pygame.display.set_icon(pygame.image.load("../assets/images/naveEspacial4.png"))

fonte = pygame.font.SysFont("arial", 20, True, False)

nave_jogador = NaveJogador(
    imagem= "../assets/images/naveEspacial5.png",
    velocidade=settings["NaveJogador"]["velocidade"], 
    posicao=[350, 400], 
    pontos_vida=100, 
    potencia_tiro=10, 
    tempo_recarga=1.5, 
    aprimoramentos={}
)

naves_inimigas = niveis.gerar_niveis(surface, 5)

def inicio_jogo():
    global estado
    tempo_inicial = pygame.time.get_ticks() 

    usuarios = manipularArquivos.carregar_usuarios()
    top_usuarios = usuarios.nlargest(3, 'pontos')

    run = True
    while run:
        if estado == TELA_INICIAL:
            if pygame.time.get_ticks() - tempo_inicial <= 1000:
                telas.desenha_tela_inicial(surface)
            else:
                estado = MENU  
        else:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if estado == MENU:
                        if event.key == pygame.K_1:    
                            estado = CONTINUAR
                        elif event.key == pygame.K_2: 
                            estado = NOVO_JOGO  
                        elif event.key == pygame.K_3:  
                            estado = MELHORES_JOGADORES
                    elif event.key == pygame.K_ESCAPE:
                        estado = MENU
                
        if estado == MENU:
            telas.menu(surface, fonte)
        elif estado == CONTINUAR:
            telas.novo_jogo(surface,nave_jogador, naves_inimigas, screen_width, screen_height)

        elif estado == NOVO_JOGO:
            estado = telas.add_usuario(surface, usuarios, fonte)

        elif estado == MELHORES_JOGADORES:
            estado = telas.melhores_jogadores(surface, top_usuarios)

        pygame.display.flip()

    pygame.quit()

inicio_jogo()
