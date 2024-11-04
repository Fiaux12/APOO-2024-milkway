import pygame
from naveBase import NaveBase

class NaveInimiga(NaveBase):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga, tempo_parado):
        super().__init__(imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga)
        self.tempo_parado = tempo_parado  
        self.tempo_parado_decorrido = 0  
        self.movendo = False
        


    def atirar():
        raise NotImplementedError("Este método deve ser implementado")

    def destrutor():
        raise NotImplementedError("Este método deve ser implementado")

    def retacionarImagem(self):
        self.imagem = pygame.transform.rotate(self.imagem, 180)


    def update(self):
        tempo_atual = pygame.time.get_ticks()

        # Verifica se já passou o tempo de parada
        if tempo_atual >= self.tempo_parado:
            self.movendo = True

        # Movimenta a nave para baixo se a flag estiver ativada
        if self.movendo:
            self.posicao[1] += self.velocidade  # Movimenta para baixo conforme a velocidade
            self.rect.topleft=self.posicao      #Atualiza a colisão da nave de acordo com a posição

        # # Verifica se a nave saiu da tela e retorna um sinal para removê-la
        # if self.posicao[1] > 600:  # Suponha que 600 seja a altura da tela
        #     return True  # Retorna True se a nave deve ser removida (fora da tela)
        # return False