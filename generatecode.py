import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SampleScene")

# Color de fondo
bg_color = (255, 255, 255)

# Ciclo principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la pantalla
    screen.fill(bg_color)
    pygame.display.flip()
