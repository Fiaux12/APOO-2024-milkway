import manipularArquivos 

settings = manipularArquivos.ler_configuracoes()

# Tela
screen_width = settings["Tela"]["screen_width"]
screen_height = settings["Tela"]["screen_height"]

#Nave jogado
velocidade_jogador = settings["NaveJogador"]["velocidade"]
pontos_vida_jogador = settings["NaveJogador"]["pontos_vida"]
potencia_tiro = settings["NaveJogador"]["potencia_tiro"]
posicao_inicial = settings["NaveJogador"]["posicao_inicial"]

#Nave inimiga
velocidade_inimigo = settings["NaveInimigo"]["velocidade"]
qtd_inimigas = int(settings["NaveInimigo"]["quantidade"]) 
tempo_geracao = int(settings["NaveInimigo"]["tempo_geracao"])
pontos_vida_inimigo = settings["NaveInimigo"]["pontos_vida"]
posicao_inicial_y = settings["NaveInimigo"]["posicao_inicial_y"]

#Nave inimiga
tempo_tela_inicial = settings["Tempos"]["tela_inicial"]
tempo_tela_game_over = settings["Tempos"]["tempo_tela_game_over"]
tempo_tela_ganhador = settings["Tempos"]["tempo_tela_ganhador"]

#Geral
powerUp_velocidade = settings["Geral"]["powerUp_velocidade"]
powerUp_potencia_tiro = settings["Geral"]["powerUp_potencia_tiro"]
