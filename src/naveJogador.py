import pygame
from naveBase import NaveBase
from bullet import Bullet
import settings 

class NaveJogador(NaveBase):
    def __init__(self, imagem, velocidade, posicao, pontos_vida, potencia_tiro, aprimoramentos):
        super().__init__(imagem, velocidade, posicao, pontos_vida)
        self.potencia_tiro = potencia_tiro
        self.aprimoramentos = aprimoramentos
        self.bullets = []
        self.space_pressed = False
        self.rect = self.imagem.get_rect(topleft=posicao)

    def atira(self):
        bullet = Bullet(self.posicao, self.potencia_tiro, "../assets/images/asteroideAzul1.png", 1)
        self.bullets.append(bullet)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(surface)

    def update(self, surface):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.posicao[0] > 0:
            self.posicao[0] -= self.velocidade
            self.rect.topleft=self.posicao
            self.rect.inflate_ip(-10, -10)
        if teclas[pygame.K_RIGHT] and self.posicao[0] < (settings.screen_width + 180) - self.imagem.get_width():
            self.posicao[0] += self.velocidade
            self.rect.topleft=self.posicao
            self.rect.inflate_ip(-10, -10)
        if teclas[pygame.K_DOWN] and self.posicao[1] < (settings.screen_height + 180) - self.imagem.get_height():
            self.posicao[1] += self.velocidade
            self.rect.topleft=self.posicao
            self.rect.inflate_ip(-10, -10)
        if teclas[pygame.K_UP] and self.posicao[1] > 0:
            self.posicao[1] -= self.velocidade
            self.rect.topleft=self.posicao
            self.rect.inflate_ip(-10, -10)

        #Gera e desenha novo tiro
        if teclas[pygame.K_SPACE]:
            if not self.space_pressed:
                self.atira()
                self.space_pressed = True
        else:
            self.space_pressed = False
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(surface)

        #Redimenciona e desenha a nave
        nave_jogador_redimensionada = pygame.transform.scale(self.imagem, (100, 100))
        self.rect = nave_jogador_redimensionada.get_rect(topleft=self.posicao)
        surface.blit(nave_jogador_redimensionada, self.posicao)
