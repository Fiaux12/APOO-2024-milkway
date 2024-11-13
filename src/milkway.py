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
GAME_OVER = "game_over"
WINNER = "winner"
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

qtd_inimigas = int(settings["QtdInimigos"]["valor"]) 


def inicio_jogo():
    global estado
    global naves_inimigas 
    tempo_inicial = pygame.time.get_ticks() 
    tempo_game_over = None
    tempo_winner = None
    naves_inimigas = niveis.gerar_niveis(surface, qtd_inimigas, 30)
    usuarios = manipularArquivos.carregar_usuarios()
    usuario_atual = None
    score = 0
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
                            estado = NOVO_JOGO  
                        elif event.key == pygame.K_2: 
                            estado = MELHORES_JOGADORES
                    elif event.key == pygame.K_ESCAPE:
                        estado = MENU
                
        if estado == MENU:
            telas.menu(surface, fonte)

        elif estado == CONTINUAR:
            nave_jogador.pontos_vida = 100
            valor = None
            valor = telas.novo_jogo(surface,nave_jogador, naves_inimigas, screen_width, screen_height, fonte, score)
            if valor == GAME_OVER:
                usuario_atual.pontos = score
                usuario_atual.atualizar()
                score = 0
                naves_inimigas = niveis.gerar_niveis(surface, qtd_inimigas, 30)
                tempo_game_over = pygame.time.get_ticks()
                estado = GAME_OVER

            else: 
                score = valor
                usuario_atual.pontos = valor
                usuario_atual.atualizar()

                ganhar = qtd_inimigas * 10
                if score == ganhar:
                    naves_inimigas = niveis.gerar_niveis(surface, qtd_inimigas, 30)
                    tempo_winner = pygame.time.get_ticks()
                    score = 0
                    estado = WINNER


        elif estado == NOVO_JOGO:
            estado, usuario_atual = telas.add_usuario(surface, usuarios, fonte)

        elif estado == MELHORES_JOGADORES:
            usuarios = manipularArquivos.carregar_usuarios()
            top_usuarios = usuarios.nlargest(3, 'pontos')
            estado = telas.melhores_jogadores(surface, top_usuarios)

        elif estado == GAME_OVER:
            if tempo_game_over is not None:
                tempo_decorrido = pygame.time.get_ticks() - tempo_game_over
                if tempo_decorrido <= 5000:  
                    telas.desenha_tela_game_over(surface)
                else:
                    tempo_game_over = None 
                    estado = MENU  

        elif estado == WINNER:
            if tempo_winner is not None:
                tempo_decorrido = pygame.time.get_ticks() - tempo_winner
                if tempo_decorrido <= 5000:  
                    telas.desenha_tela_ganhador(surface)
                else:
                    tempo_winner = None 
                    estado = MENU  

        pygame.display.flip()

    pygame.quit()

inicio_jogo()
