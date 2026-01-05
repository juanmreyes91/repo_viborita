import pygame
pygame.init()

#Constantes
FPS = 10
ANCHO = 400
ALTO = 360

window = pygame.Display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
run = True


while run:
  clock.tick(FPS)
  for events in pygame.
