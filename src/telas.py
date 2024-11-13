import pygame
import manipularArquivos 
from powerUp import PowerUp
from usuario import Usuario
import time
import settings
import random 

#powerUpVel = PowerUp(
#    imagem="../assets/images/powerupVEL.png",
#    posicao=[200, 300],
#    tipo='vel',
#    valor=0.5  
#)

#powerUpTiro = PowerUp(
#    imagem="../assets/images/powerupTIRO.png",
#    posicao=[800, 300],
#    tipo='tiro',
#    valor=10 
#)

powerUps = []

# Estados do jogo
TELA_INICIAL = "tela_inicial"
MENU = "menu"
NOVO_JOGO = "novo_jogo"
CONTINUAR = "continuar"
MELHORES_JOGADORES = "melhores_jogadores"
GAME_OVER = "game_over"
WINNER = "winner"

#Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0 , 0, 129)

#Fonte

#configurações do jogo
settings = manipularArquivos.ler_configuracoes()

# Carregar imagens
background = pygame.image.load("../assets/images/espaço.gif")
tela_inicial = pygame.image.load("../assets/images/NovoLogo.jpg")
tela_melhores_jogadores = pygame.image.load("../assets/images/melhoresJogadores.png")
tela_criar_usuario = pygame.image.load("../assets/images/criarUsuario.png")
tela_menu = pygame.image.load("../assets/images/menu.png")
tela_game_over = pygame.image.load("../assets/images/game_over.png")



# Retângulos para os botões
botao_continuar = pygame.Rect(350, 200, 250, 50)
botao_novo_jogo = pygame.Rect(350, 300, 250, 50)
botao_melhores_jogadores = pygame.Rect(350, 400, 250, 50)
botao_voltar = pygame.Rect(20, 540, 80, 30)


def desenhar_texto(texto, fonte, cor, pos, surface):
    text_surface = fonte.render(texto, True, cor)
    surface.blit(text_surface, pos)


def menu(surface, fonte):
    surface.blit(tela_menu, (0, 0))
    fonte_titulo = pygame.font.SysFont("arial", 50, True, False)
    desenhar_texto("MILKWAY", fonte_titulo, BRANCO, (360, 210), surface)
    
    pygame.draw.rect(surface, BRANCO, botao_novo_jogo)
    desenhar_texto("1. Novo Jogo", fonte, PRETO, (botao_novo_jogo.x + 65, botao_novo_jogo.y + 10),surface)
    
    pygame.draw.rect(surface, BRANCO, botao_melhores_jogadores)
    desenhar_texto("2. Melhores Jogadores", fonte, PRETO, (botao_melhores_jogadores.x + 20, botao_melhores_jogadores.y + 10),surface)


def novo_jogo(surface, nave_jogador, naves_inimigas, score, fonte):
    teclas = pygame.key.get_pressed()

    surface.blit(background, (0, 0))
    desenhar_texto(f"SCORE: {score}", fonte, BRANCO, (30, 30), surface)
    nave_jogador.update(surface)
    
    for nave_inimiga in naves_inimigas[:]: 
        nave_inimiga.update(nave_jogador)  
        surface.blit(nave_inimiga.imagem, nave_inimiga.posicao) 
        if nave_jogador.pontos_vida <= 0:
            if nave_inimiga.destruida:
                naves_inimigas.remove(nave_inimiga)
            return GAME_OVER

    for powerUp in powerUps:
        if powerUp.coletado == False:
            powerUp.draw(surface)
            powerUp.checar_colisao(nave_jogador)

    score = checar_colisao_bala_nave(nave_jogador.bullets, nave_jogador.potencia_tiro, naves_inimigas,score)
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


def add_usuario(surface,usuarios,fonte):
    global active, text, color
    input_box = pygame.Rect(80, 320, 320, 35) 
    active = True  
    texto = '' 
    tamanho_max_nome = 10

    while active:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    return MENU, None
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
                        return CONTINUAR, usuario
                elif event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]  
                elif len(texto) < tamanho_max_nome:
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


def checar_colisao_bala_nave(balas, potencia_tiro, naves_inimigas, score):
    balas_para_remover = []
    naves_para_remover = []

    for bala in balas:
        for nave in naves_inimigas:
            if bala.rect.colliderect(nave.rect):
                nave.pontos_vida -= potencia_tiro 
                print(potencia_tiro)

                if bala not in balas_para_remover:
                    balas_para_remover.append(bala)

                if nave.pontos_vida <= 0 and nave not in naves_para_remover:
                    naves_para_remover.append(nave)
                    score += 10
                    chance = random.randint(1, 100)
                    if chance <= 20:  # 20% de chance de aparecer um power-up
                        tipo_power_up = random.choice(['vel', 'tiro'])  # Escolhe entre velocidade ou tiro
                        if tipo_power_up == 'vel':
                            novo_power_up = PowerUp(
                                imagem="../assets/images/powerupVEL.png",
                                posicao=nave.posicao,  # Usa a posição da nave destruída
                                tipo='vel',
                                valor=0.5 #em quanto incrementa a velocidade
                            )
                        else:
                            novo_power_up = PowerUp(
                                imagem="../assets/images/powerupTIRO.png",
                                posicao=nave.posicao,  # Usa a posição da nave destruída
                                tipo='tiro',
                                valor=10 #em quanto incrementa o tiro
                            )
                        powerUps.append(novo_power_up)  # Adiciona o power-up à lista


                break  

    for bala in balas_para_remover:
        balas.remove(bala)

    for nave in naves_para_remover:
        naves_inimigas.remove(nave)

    return score
    

def desenha_tela_game_over(surface):
    surface.blit(tela_game_over, (0, 0))
    
def desenha_tela_ganhador(surface):
    surface.blit(tela_melhores_jogadores, (0, 0))
    fonte = pygame.font.SysFont("arial", 60, True, False)

    desenhar_texto("Vitória épica!!!", fonte, BRANCO, (180, 300),surface)


    
    
