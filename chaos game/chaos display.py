import pygame
import sys

from pygame.constants import FULLSCREEN
from chaos import Chaos


WIDTH =800
HEIGHT = 800
Chaos = Chaos(HEIGHT,WIDTH,3)
pygame.init()
pygame.display.set_caption('Chaos Game')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def update(screen):
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        screen.fill((0,0,0))
        for i in Chaos.vertex:
            pygame.draw.circle(screen,i[2],(i[0],i[1]),3)
        for i in range(1000000):
            point,colour = Chaos.create_point()
            pygame.draw.circle(screen,colour,point,1)
            pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    update(screen)
