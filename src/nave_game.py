import pygame
import random
import sys

# Inicializar o pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensões da tela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Naves")

# Carregar imagens
player_image = pygame.image.load("../assets/images/naveEspacial.png")
enemy_image = pygame.image.load("../assets/images/naveEspacial.png") 
bullet_image = pygame.image.load("../assets/images/asteroideAzul1.png") 

# Classe para a nave do jogador
class Player:
    def __init__(self):
        self.image = player_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150))
        self.speed = 5
        self.bullets = []

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(bullet)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(surface)

class Bullet:
    def __init__(self, x, y):
        self.image = bullet_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Classe para os inimigos
class Enemy:
    def __init__(self):
        self.image = enemy_image
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH - 50), -50))
        self.speed = random.randint(2, 5)

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Função principal do jogo
def game():
    player = Player()
    enemies = []
    score = 0
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()

        player.move()

        # Atualizar e desenhar os tiros
        for bullet in player.bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                player.bullets.remove(bullet)

        # Criar inimigos
        if random.randint(1, 30) == 1:
            enemies.append(Enemy())

        # Atualizar e desenhar inimigos
        for enemy in enemies[:]:
            enemy.move()
            if enemy.rect.top > SCREEN_HEIGHT:
                enemies.remove(enemy)
            for bullet in player.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    player.bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break

        # Desenhar nave do jogador, tiros e inimigos
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # Exibir pontuação
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()
