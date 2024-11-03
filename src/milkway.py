import pygame
from usuario import Usuario
from naveJogador import NaveJogador
import niveis 
import manipularArquivos 
import telas 
import time


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

#fonte
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
                            estado = CONTINUAR
                        elif telas.botao_novo_jogo.collidepoint(mouse_pos):
                            estado = NOVO_JOGO  
                        elif telas.botao_melhores_jogadores.collidepoint(mouse_pos):
                            estado = MELHORES_JOGADORES
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            estado = MENU
                
        #TODO colocar o estado de NOVO_JOGO em uma função
        # Desenhar a tela correspondente ao estado atual
        if estado == MENU:
            telas.menu(surface, fonte)
        elif estado == CONTINUAR:
            telas.novo_jogo(surface,nave_jogador, naves_inimigas, screen_width, screen_height)
        elif estado == NOVO_JOGO:
            global active, text, color
            input_box = pygame.Rect(80, 320, 320, 35) 
            active = True  
            texto = '' 

            while active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_box.collidepoint(event.pos):
                            active = not active
                        else:
                            active = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if  texto in usuarios['nome'].values:
                                telas.desenhar_texto("Esse nickname já existe!!!", fonte, telas.AZUL, (300,450), surface)
                                pygame.display.flip() 
                                telas.time.sleep(2) 
                            else:
                                usuario = Usuario(texto)
                                manipularArquivos.adicionar_usuario(usuario.nome, usuario.pontos, usuario.save_point)
                                telas.desenhar_texto("Nickname criado!!!", fonte, telas.AZUL, (300,450), surface)
                                active = False  
                                pygame.display.flip()  
                                telas.time.sleep(2) 
                                estado = MENU 
                            active = False  
                        elif event.key == pygame.K_BACKSPACE:
                            texto = texto[:-1]  
                        else:
                            texto += event.unicode  

                surface.blit(telas.tela_criar_usuario, (0, 0))
                pygame.draw.rect(surface, telas.BRANCO, input_box, 2)
                txt_surface = fonte.render(texto, True, telas.BRANCO)
                surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                pygame.display.flip()

        elif estado == MELHORES_JOGADORES:
            telas.melhores_jogadores(surface, top_usuarios)

        pygame.display.flip()

    pygame.quit()

inicio_jogo()
