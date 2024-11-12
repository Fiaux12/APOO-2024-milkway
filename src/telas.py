import pygame
import manipularArquivos 
from naveJogador import NaveJogador
from powerUp import PowerUp
from usuario import Usuario
import niveis 
import time

powerUpVel = PowerUp(
    imagem="../assets/images/powerupVEL.png",
    posicao=[200, 300],
    tipo='vel',
    valor=0.5  # Aumenta a velocidade em 0.5 unidades
)

powerUpTiro = PowerUp(
    imagem="../assets/images/powerupTIRO.png",
    posicao=[800, 300],
    tipo='potencia_tiro',
    valor=1  # Aumenta a potência do tiro em 1 unidade
)

powerUps = [powerUpVel,powerUpTiro]


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
tela_criar_usuario = pygame.image.load("../assets/images/criarUsuario.png")
tela_menu = pygame.image.load("../assets/images/menu.png")


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
    surface.blit(tela_menu, (0, 0))
    
    desenhar_texto("MILKWAY", fonte, BRANCO, (425, 100), surface)
    
    pygame.draw.rect(surface, BRANCO, botao_continuar)
    desenhar_texto("1. Continuar", fonte, PRETO, (botao_continuar.x + 75, botao_continuar.y + 10),surface)
    
    pygame.draw.rect(surface, BRANCO, botao_novo_jogo)
    desenhar_texto("2. Novo Jogo", fonte, PRETO, (botao_novo_jogo.x + 65, botao_novo_jogo.y + 10),surface)
    
    pygame.draw.rect(surface, BRANCO, botao_melhores_jogadores)
    desenhar_texto("3. Melhores Jogadores", fonte, PRETO, (botao_melhores_jogadores.x + 20, botao_melhores_jogadores.y + 10),surface)


def novo_jogo(surface, nave_jogador, naves_inimigas, screen_width, screen_height, fonte, score):
    teclas = pygame.key.get_pressed()

    surface.blit(background, (0, 0))
    desenhar_texto(f"SCORE: {score}", fonte, BRANCO, (30, 30), surface)
    nave_jogador.update(screen_width, screen_height, surface)

    for nave in naves_inimigas[:]:  
        nave.update(nave_jogador)  
        surface.blit(nave.imagem, nave.posicao) 

    for powerUp in powerUps:
        if powerUp.coletado == False:
            powerUp.draw(surface)
            powerUp.checar_colisao(nave_jogador)

    score = checar_colisao_bala_nave(nave_jogador.bullets ,naves_inimigas,score)
    pygame.display.flip()
    return score




def melhores_jogadores(surface, top_usuarios):
    fonte_titulo = pygame.font.SysFont("arial", 30, True, False)
    fonte_texto = pygame.font.SysFont("arial", 25, True, False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return MENU
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    return MENU

        surface.fill((255, 255, 255))
        surface.blit(tela_melhores_jogadores, (0, 0))
        pygame.draw.polygon(surface, AZUL, 
           [(45, 600 - 40),     
            (75, 600 - 65),      
            (75, 600 - 15)])
        
        desenhar_texto("Melhores Jogadores", fonte_titulo, AZUL, (45, 73), surface)
        desenhar_texto("Nome", fonte_texto, AZUL, (45, 290), surface)
        desenhar_texto("Naves abatidas", fonte_texto, AZUL, (500, 290), surface)

        posicao_y = 300
        for index, usuario in top_usuarios.iterrows():
            posicao_y += 50
            nome = usuario["nome"]
            pontos = usuario["pontos"]
            texto = f".............................................................. {pontos}"
            desenhar_texto(nome, fonte_texto, AZUL, (45, posicao_y), surface)
            desenhar_texto(texto, fonte_texto, AZUL, (160, posicao_y), surface)

        pygame.display.flip()


def add_usuario(surface,usuarios, fonte):
    global active, text, color
    input_box = pygame.Rect(80, 320, 320, 35) 
    active = True  
    texto = '' 
    max_nome = 10        

    while active:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    return MENU
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if  texto in usuarios['nome'].values:
                        desenhar_texto("Esse nickname já existe!!!", fonte, AZUL, (300,450), surface)
                        pygame.display.flip() 
                        time.sleep(2) 
                    else:
                        usuario = Usuario(texto)
                        manipularArquivos.adicionar_usuario(usuario.nome, usuario.pontos, usuario.save_point)
                        desenhar_texto("Nickname criado!!!", fonte, AZUL, (300,450), surface)
                        active = False  
                        pygame.display.flip()  
                        time.sleep(2) 
                        return MENU 
                    active = False  
                elif event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]  
                elif len(texto) < max_nome:
                    texto += event.unicode  

        
        
        surface.blit(tela_criar_usuario, (0, 0))
        pygame.draw.polygon(surface, AZUL, 
            [(45, 600 - 40),     
            (75, 600 - 65),      
            (75, 600 - 15)])
        pygame.draw.rect(surface, BRANCO, input_box, 2)
        txt_surface = fonte.render(texto, True, BRANCO)
        surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

def desenha_tela_inicial(surface):
    surface.blit(tela_inicial, (0, -200))


def checar_colisao_bala_nave(balas, naves_inimigas, score):
    balas_para_remover = []
    naves_para_remover = []

    for bala in balas:
        for nave in naves_inimigas:
            if bala.rect.colliderect(nave.rect):
                nave.pontos_vida -= 10 
                print(nave.pontos_vida) 

                if bala not in balas_para_remover:
                    balas_para_remover.append(bala)

                if nave.pontos_vida <= 0 and nave not in naves_para_remover:
                    naves_para_remover.append(nave)
                    score += 10

                break  

    for bala in balas_para_remover:
        balas.remove(bala)

    for nave in naves_para_remover:
        naves_inimigas.remove(nave)

    return score
