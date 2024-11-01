import pygame
import values
from naveJogador import NaveJogador
from naveInimiga import NaveInimiga
from usuario import Usuario
import manipularArquivos 
import niveis 
import telas 


pygame.init()
# Estados do jogo
TELA_INICIAL = "tela_inicial"
MENU = "menu"
JOGO = "jogo"
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

# Criação de uma instância da NaveJogador
nave_jogador = NaveJogador(
    imagem= "../assets/images/naveEspacial5.png",
    velocidade=settings["NaveJogador"]["velocidade"], 
    posicao=[350, 400], 
    pontos_vida=100, 
    potencia_tiro=10, 
    tempo_recarga=1.5, 
    aprimoramentos={}
)


naves_inimigas = niveis.nivel1(surface)


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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if estado == MENU:
                        if telas.botao_continuar.collidepoint(mouse_pos):
                            estado = JOGO
                        elif telas.botao_novo_jogo.collidepoint(mouse_pos):
                            estado = JOGO  
                        elif telas.botao_melhores_jogadores.collidepoint(mouse_pos):
                            estado = MELHORES_JOGADORES
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            estado = MENU

        # Desenhar a tela correspondente ao estado atual
        if estado == MENU:
            telas.menu(surface, fonte)
        elif estado == JOGO:
            telas.novo_jogo(surface, nave_jogador, naves_inimigas, screen_width, screen_height)
        elif estado == MELHORES_JOGADORES:
            telas.melhores_jogadores(surface, top_usuarios)

        # Desenhar fundo
        # telas.draw_background()

        

        # Atualizar a tela
        pygame.display.flip()

    pygame.quit()

# Iniciar o jogo
inicio_jogo()
