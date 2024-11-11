import pygame
from naveBase import NaveBase
from bullet import Bullet
import sys
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800


#adicionei um vetor pra guardar os bullets
#adicionei um rect pra pegar o tamnaho da tela, isso pra evitar de mexer na posição do jogador e dar aquele bug

class NaveJogador(NaveBase):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga, aprimoramentos):
        super().__init__(imagem, velocidade, posicao, pontos_vida, potencia_tiro, tempo_recarga)
        self.aprimoramentos = aprimoramentos
        self.bullets = []
        self.rect = self.imagem.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150))


    def shoot(self):
        bullet = Bullet(self.posicao[0], self.posicao[1])
        self.bullets.append(bullet)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(surface)


    def calcularAprimoramento():
        raise NotImplementedError("Este método deve ser implementado")
    
    def update(self, screen_width, screen_height, surface):
        # Verificar teclas pressionadas para movimentar a nave
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.posicao[0] > 0:
            self.posicao[0] -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.posicao[0] < (screen_width+180) - self.imagem.get_width():
            self.posicao[0] += self.velocidade
        if teclas[pygame.K_DOWN] and self.posicao[1] < (screen_height+180) - self.imagem.get_height():
            self.posicao[1] += self.velocidade
        if teclas[pygame.K_UP] and self.posicao[1] > 0:
            self.posicao[1] -= self.velocidade
        if teclas[pygame.K_SPACE]:
            self.shoot()
        
        nave_jogador_redimensionada = pygame.transform.scale(self.imagem, (100, 100))
        surface.blit(nave_jogador_redimensionada, self.posicao)
