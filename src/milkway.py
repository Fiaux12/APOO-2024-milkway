import pygame
from naveJogador import NaveJogador
import niveis 
import manipularArquivos 
import telas 
import settings 

pygame.init()

# Estados do jogo
estado = telas.TELA_INICIAL

# Cria tela do Pygame
surface = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('MilkWay')
pygame.display.set_icon(pygame.image.load("../assets/images/naveEspacial4.png"))

fonte = pygame.font.SysFont("arial", 20, True, False)

nave_jogador = NaveJogador(
    imagem = "../assets/images/naveEspacial5.png",
    velocidade = settings.velocidade_jogador, 
    posicao = settings.posicao_inicial, 
    pontos_vida = settings.pontos_vida_jogador, 
    potencia_tiro = settings.potencia_tiro, 
    aprimoramentos = {}
)


def inicio_jogo():
    global estado
    global naves_inimigas 
    tempo_inicial = pygame.time.get_ticks() 
    tempo_game_over = None
    tempo_winner = None
    naves_inimigas = niveis.gerar_niveis(surface)
    usuarios = manipularArquivos.carregar_usuarios()
    usuario_atual = None
    score = 0
    run = True
    while run:

        if estado == telas.TELA_INICIAL:
            if pygame.time.get_ticks() - tempo_inicial <= settings.tempo_tela_inicial:
                telas.desenha_tela_inicial(surface)
            else:
                estado = telas.MENU  
        else:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if estado == telas.MENU:
                        if event.key == pygame.K_1:    
                            estado = telas.NOVO_JOGO  
                        elif event.key == pygame.K_2: 
                            estado = telas.MELHORES_JOGADORES
                    elif event.key == pygame.K_ESCAPE:
                        estado = telas.MENU
                
        if estado == telas.MENU:
            telas.menu(surface, fonte)

        elif estado == telas.CONTINUAR:
            nave_jogador.pontos_vida = settings.pontos_vida_jogador
            valor = None
            valor = telas.novo_jogo(surface, nave_jogador, naves_inimigas, score, fonte)
            if valor == telas.GAME_OVER or (score == 0 and len(naves_inimigas) == 0):
                usuario_atual.pontos = score
                usuario_atual.atualizar()
                tempo_game_over = pygame.time.get_ticks()
                naves_inimigas = niveis.gerar_niveis(surface)
                score = 0
                nave_jogador.bullets = []
                estado = telas.GAME_OVER

            else: 
                score = valor
                usuario_atual.pontos = valor
                usuario_atual.atualizar()

                pontos = settings.qtd_inimigas * 10
                if score == pontos or len(naves_inimigas) == 0:
                    naves_inimigas = niveis.gerar_niveis(surface)
                    score = 0
                    nave_jogador.bullets = []
                    tempo_winner = pygame.time.get_ticks()
                    estado = telas.WINNER


        elif estado == telas.NOVO_JOGO:
            estado, usuario_atual = telas.add_usuario(surface, usuarios, fonte)

        elif estado == telas.MELHORES_JOGADORES:
            usuarios = manipularArquivos.carregar_usuarios()
            top_usuarios = usuarios.nlargest(3, 'pontos')
            estado = telas.melhores_jogadores(surface, top_usuarios)

        elif estado == telas.GAME_OVER:
            if tempo_game_over is not None:
                tempo_decorrido = pygame.time.get_ticks() - tempo_game_over
                if tempo_decorrido <= settings.tempo_tela_game_over:  
                    telas.desenha_tela_game_over(surface)
                else:
                    tempo_game_over = None 
                    estado = telas.MENU  

        elif estado == telas.WINNER:
            if tempo_winner is not None:
                tempo_decorrido = pygame.time.get_ticks() - tempo_winner
                if tempo_decorrido <= settings.tempo_tela_ganhador:  
                    telas.desenha_tela_ganhador(surface)
                else:
                    tempo_winner = None 
                    estado = telas.MENU  

        pygame.display.flip()

    pygame.quit()

inicio_jogo()
