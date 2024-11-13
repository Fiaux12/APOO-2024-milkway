import pygame
from naveBase import NaveBase

class NaveInimiga(NaveBase):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga, tempo_parado):
        super().__init__(imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga)
        self.tempo_parado = tempo_parado  
        self.tempo_parado_decorrido = 0  
        self.movendo = False
        self.rect = self.imagem.get_rect(topleft=posicao)
        self.destruida = False


    def checar_colisao(self, nave_jogador):
        if self.rect.colliderect(nave_jogador.rect):
            nave_jogador.pontos_vida -= 100 
            self.destruida = True 
            return True
        
        return False

    def retacionarImagem(self):
        self.imagem = pygame.transform.rotate(self.imagem, 180)


    def update(self,nave_jogador):
        tempo_atual = pygame.time.get_ticks()

        if tempo_atual >= self.tempo_parado:
            self.movendo = True

        if self.movendo:
            self.posicao[1] += self.velocidade  
            self.rect.topleft=self.posicao     
       
        return self.checar_colisao(nave_jogador)


        # # Verifica se a nave saiu da tela e retorna um sinal para removê-la
        # if self.posicao[1] > 600:  # Suponha que 600 seja a altura da tela
        #     return True  # Retorna True se a nave deve ser removida (fora da tela)
        # return False

    def __del__(self):
        print(f"Destruindo a nave inimiga.")
