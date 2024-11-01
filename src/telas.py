import pygame
import manipularArquivos 


# Estados do jogo
TELA_INICIAL = "tela_inicial"
MENU = "menu"
JOGO = "jogo"
MELHORES_JOGADORES = "melhores_jogadores"
estado = TELA_INICIAL

#configurações do jogo
settings = manipularArquivos.ler_configuracoes()

# Carregar imagens
background = pygame.image.load("../assets/images/espaço.gif")
tela_inicial = pygame.image.load("../assets/images/NovoLogo.jpg")
tela_melhores_jogadores = pygame.image.load("../assets/images/melhoresJogadores.png")


#Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Retângulos para os botões
botao_continuar = pygame.Rect(350, 200, 250, 50)
botao_novo_jogo = pygame.Rect(350, 300, 250, 50)
botao_melhores_jogadores = pygame.Rect(350, 400, 250, 50)


def draw_background(surface):
    surface.blit(background, (0, 0))


def desenhar_texto(texto, fonte, cor, pos, surface):
    text_surface = fonte.render(texto, True, cor)
    surface.blit(text_surface, pos)


def menu(surface, fonte):
    surface.fill(PRETO)
    
    desenhar_texto("MILKWAY", fonte, BRANCO, (425, 100), surface)
    
    pygame.draw.rect(surface, BRANCO, botao_continuar)
    desenhar_texto("Continuar", fonte, PRETO, (botao_continuar.x + 80, botao_continuar.y + 10),surface)
    
    pygame.draw.rect(surface, BRANCO, botao_novo_jogo)
    desenhar_texto("Novo Jogo", fonte, PRETO, (botao_novo_jogo.x + 70, botao_novo_jogo.y + 10),surface)
    
    pygame.draw.rect(surface, BRANCO, botao_melhores_jogadores)
    desenhar_texto("Melhores Jogadores", fonte, PRETO, (botao_melhores_jogadores.x + 30, botao_melhores_jogadores.y + 10),surface)


def jogo(surface, fonte):
    surface.fill(PRETO)
    desenhar_texto("Tela do Jogo", fonte, BRANCO, (350, 250),surface)


def melhores_jogadores(surface):
    fonte = pygame.font.SysFont("arial", 30, True, False)
    surface.blit(tela_melhores_jogadores, (0, 0))

    desenhar_texto("Melhores Jogadores", fonte, (255,215,0), (45, 73),surface)


def desenha_tela_inicial(surface):
    surface.blit(tela_inicial, (0, -200))
    

    