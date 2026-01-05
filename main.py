import pygame
pygame.init()

#Constantes
FPS = 10
ANCHO = 400
ALTO = 360

window = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
run = True
direction = (10, 0)

snake = pygame.Rect((0, 0),(10, 10))
colour_snake = pygame.Surface((10, 10))
colour_snake.fill((0, 255, 0))


while run:
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        pass
      if event.key == pygame.K_DOWN:
        pass
      if event.key == pygame.K_RIGHT:
        pass
      if event.key == pygame.K_LEFT:
        pass
  window.fill((0, 0, 0))
  window.blit(colour_snake, snake)
  pygame.display.update()

pygame.quit()