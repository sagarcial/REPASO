import pygame
import sys

class Dibujable:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def dibujar(self, pantalla):
        pass

class Triangulo(Dibujable):
    def dibujar(self, pantalla):
        pygame.draw.polygon(pantalla, (255, 0, 0), [self.punto1, self.punto2, (self.punto1[0], self.punto2[1])])

class Circulo(Dibujable):
    def dibujar(self, pantalla):
        radio = int(((self.punto1[0] - self.punto2[0]) ** 2 + (self.punto1[1] - self.punto2[1]) ** 2) ** 0.5 * 0.5)  # Modificar el radio aquí (0.5 es el factor)
        pygame.draw.circle(pantalla, (0, 255, 0), self.punto1, radio)

class Rectangulo(Dibujable):
    def dibujar(self, pantalla):
        ancho = abs(self.punto1[0] - self.punto2[0])
        alto = abs(self.punto1[1] - self.punto2[1])
        pygame.draw.rect(pantalla, (0, 0, 255), (self.punto1[0], self.punto1[1], ancho, alto))

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Dibujar Figuras')

figuras = []

punto1 = None
punto2 = None
dibujando = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if not dibujando:
                punto1 = evento.pos
                dibujando = True
            else:
                punto2 = evento.pos
                dibujando = False
                figura = None
                if pygame.key.get_pressed()[pygame.K_t]:
                    figura = Triangulo(punto1, punto2)
                elif pygame.key.get_pressed()[pygame.K_c]:
                    figura = Circulo(punto1, punto2)
                elif pygame.key.get_pressed()[pygame.K_r]:
                    figura = Rectangulo(punto1, punto2)
                if figura:
                    figuras.append(figura)
    pantalla.fill((255, 255, 255))
    for figura in figuras:
        figura.dibujar(pantalla)
    if dibujando:
        pygame.draw.rect(pantalla, (0, 0, 0), (punto1[0], punto1[1], pygame.mouse.get_pos()[0] - punto1[0], pygame.mouse.get_pos()[1] - punto1[1]), 1)
    pygame.display.flip()
