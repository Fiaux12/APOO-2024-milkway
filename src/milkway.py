import pygame
import values
from naveJogador import NaveJogador
from naveInimiga import NaveInimiga
from usuario import Usuario
import manipularArquivos 
from powerUp import powerUp

pygame.init()

#settings = manipularArquivos.ler_configuracoes()
settings = {
    "Tela": {
        "screen_width": 900,
        "screen_height": 500
    },
    "NaveJogador": {
        "velocidade" : 0.5,
        "pontos_vida" : 100,
        "potencia_tiro" : 100,
        "tempo_recarga" : 100
    }
}


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
powerUpVel = powerUp(
    imagem="../assets/images/powerUpVEL.png",
    posicao=[200, 300],
    tipo='vel',
    valor=2  # Aumenta a velocidade em 2 unidades
)

powerUpTiro = powerUp(
    imagem="../assets/images/powerupTIRO.png",
    posicao=[800, 300],
    tipo='potencia_tiro',
    valor=5  # Aumenta a potência do tiro em 5 unidades
)
powerUps = [powerUpVel,powerUpTiro]
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
            nave_jogador.rect.topleft = nave_jogador.posicao
        if teclas[pygame.K_RIGHT] and nave_jogador.posicao[0] < screen_width - nave_jogador.imagem.get_width():
            nave_jogador.posicao[0] += nave_jogador.velocidade
            nave_jogador.rect.topleft = nave_jogador.posicao
        if teclas[pygame.K_UP] and nave_jogador.posicao[1] > 0:
            nave_jogador.posicao[1] -= nave_jogador.velocidade
            nave_jogador.rect.topleft = nave_jogador.posicao
        if teclas[pygame.K_DOWN] and nave_jogador.posicao[1] < screen_height - nave_jogador.imagem.get_height():
            nave_jogador.posicao[1] += nave_jogador.velocidade
            nave_jogador.rect.topleft = nave_jogador.posicao

        # Desenhar a nave do jogador
        surface.blit(nave_jogador.imagem, nave_jogador.posicao)
        for powerUp in powerUps:
            if powerUp.coletado==False:
                powerUp.draw(surface)
                powerUp.checar_colisao(nave_jogador)
        # Atualizar a tela
        pygame.display.flip()

    pygame.quit()

# Iniciar o jogo
inicio_jogo()
