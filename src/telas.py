import pygame
import manipularArquivos 
from posicao import Posicao



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
AZUL = (0 , 0, 129)

# Retângulos para os botões
botao_continuar = pygame.Rect(350, 200, 250, 50)
botao_novo_jogo = pygame.Rect(350, 300, 250, 50)
botao_melhores_jogadores = pygame.Rect(350, 400, 250, 50)


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


def novo_jogo(surface, nave_jogador, naves_inimigas, screen_width, screen_height):
    surface.blit(background, (0, 0))
    #Atualiza os movimentos do jogador
    nave_jogador.update(screen_width, screen_height, surface)

    for nave in naves_inimigas[:]:  
        nave.update()  
        surface.blit(nave.imagem, nave.posicao) 

def melhores_jogadores(surface, top_usuarios):
    fonte_titulo = pygame.font.SysFont("arial", 30, True, False)
    fonte_texto = pygame.font.SysFont("arial", 25, True, False)
    surface.blit(tela_melhores_jogadores, (0, 0))

    desenhar_texto("Melhores Jogadores", fonte_titulo, AZUL, (45, 73),surface)

    desenhar_texto("Nome", fonte_texto, AZUL, (45,290), surface)
    desenhar_texto("Naves abatidas", fonte_texto, AZUL, (500, 290), surface)

    posicao_y = 300
    for index, usuario in top_usuarios.iterrows():
        posicao_y += 50
        nome = usuario["nome"]
        pontos = usuario["pontos"]
        
        texto = f".............................................................. {pontos}"
        desenhar_texto(nome, fonte_texto, AZUL, (45, posicao_y), surface)
        desenhar_texto(texto, fonte_texto, AZUL, (160, posicao_y), surface)




def desenha_tela_inicial(surface):
    surface.blit(tela_inicial, (0, -200))
    

    