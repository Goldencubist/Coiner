import pygame
import random
pygame.init()
pygame.font.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Coiner")
rodando = True
posicao_x = 400
posicao_y = 300
moeda_x = random.randint(1, largura_tela)
moeda_y = random.randint(1, altura_tela)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
pontuacao = 0
tempo_do_ultimo_combo = 0
multiplicador_combo = 1
fonte = pygame.font.SysFont('Arial', 30)
while rodando:
    temporodando = pygame.time.get_ticks()
    key = pygame.key.get_pressed()
    distancia = ((posicao_x - moeda_x)**2 + (posicao_y - moeda_y)**2)**0.5
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    if key[pygame.K_a]:
        posicao_x -= 0.5
    if key[pygame.K_d]:
        posicao_x += 0.5
    if key[pygame.K_w]:
        posicao_y -= 0.5
    if key[pygame.K_s]:
        posicao_y += 0.5
    if posicao_y >= altura_tela:
        posicao_y = 1
    if posicao_y <= 0:
        posicao_y = (altura_tela - 1)
    if posicao_x <= 0:
        posicao_x = (largura_tela - 1)
    if posicao_x >= largura_tela:
        posicao_x = 1
    if distancia < 30:
        moeda_x = random.randint(1, largura_tela)
        moeda_y = random.randint(1, altura_tela)
        pontuacao += 1 * multiplicador_combo
        multiplicador_combo += 1
        tempo_do_ultimo_combo = pygame.time.get_ticks()
    if temporodando - tempo_do_ultimo_combo >= 3000:
        multiplicador_combo = 1
    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, BRANCO, (posicao_x, posicao_y), 20)
    pygame.draw.circle(tela, AMARELO, (moeda_x, moeda_y), 10)
    textodepontos = fonte.render(f'Pontos: {pontuacao}', True, BRANCO)
    texto_combo = fonte.render(f'Combo: {multiplicador_combo}x', True, (255, 255, 255))
    texto_combo_rect = texto_combo.get_rect()
    texto_combo_rect.right = largura_tela - 10
    texto_combo_rect.top = 10
    tela.blit(texto_combo, texto_combo_rect)
    tela.blit(textodepontos, (10, 10))
    pygame.display.flip()
