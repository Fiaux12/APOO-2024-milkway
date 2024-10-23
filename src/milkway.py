import pygame
import values
from naveJogador import NaveJogador
from naveInimiga import NaveInimiga
from usuario import Usuario
import manipularArquivos 


pygame.init()

settings = manipularArquivos.ler_configuracoes()

# Tela do Pygame
screen_width = settings["Tela"]["screen_width"]
screen_height = settings["Tela"]["screen_height"]
surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MilkWay')
pygame.display.set_icon(pygame.image.load("../assets/images/naveEspacial4.png"))

# Carregar imagens
background = pygame.image.load("../assets/images/espaço.gif")

# Criação de uma instância da NaveJogador
nave_jogador = NaveJogador(
    imagem= "../assets/images/naveEspacial.png",
    velocidade=settings["NaveJogador"]["velocidade"], 
    posicao=[350, 400], 
    pontos_vida=100, 
    potencia_tiro=10, 
    tempo_recarga=1.5, 
    aprimoramentos={}
)

def draw_background():
    """Desenha a imagem de fundo na tela."""
    surface.blit(background, (0, 0))

def inicio_jogo():
    run = True
    while run:
        # Lidar com eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Desenhar fundo
        draw_background()

        # Verificar teclas pressionadas para movimentar a nave
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] and nave_jogador.posicao[0] > 0:
            nave_jogador.posicao[0] -= nave_jogador.velocidade
        if teclas[pygame.K_RIGHT] and nave_jogador.posicao[0] < screen_width - nave_jogador.imagem.get_width():
            nave_jogador.posicao[0] += nave_jogador.velocidade
        if teclas[pygame.K_UP] and nave_jogador.posicao[1] > 0:
            nave_jogador.posicao[1] -= nave_jogador.velocidade
        if teclas[pygame.K_DOWN] and nave_jogador.posicao[1] < screen_height - nave_jogador.imagem.get_height():
            nave_jogador.posicao[1] += nave_jogador.velocidade

        # Desenhar a nave do jogador
        surface.blit(nave_jogador.imagem, nave_jogador.posicao)

        # Atualizar a tela
        pygame.display.flip()

    pygame.quit()

# Iniciar o jogo
inicio_jogo()
