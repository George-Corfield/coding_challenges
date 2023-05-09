import pygame
import sys
from conways import Conways

RESOLUTION = 15
WIDTH = 1000
HEIGHT = 500
conways = Conways(RESOLUTION,WIDTH,HEIGHT)
pygame.init()
pygame.display.set_caption('Conway\'s game of life')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
fps = 10



def update(screen):
    while True:
        clock.tick(fps)
        grid = conways.cgrid
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        for i in range(conways.rows):
            for j in range(conways.cols):
                x = j*RESOLUTION
                y = i*RESOLUTION
                if grid[i][j] == 1:
                    colour = (0,0,0)
                else:
                    colour = (255,255,255)
                pygame.draw.rect(screen,(0,0,0),(x-1,y-1,RESOLUTION,RESOLUTION),width=1)
                pygame.draw.rect(screen,colour,(x,y,RESOLUTION,RESOLUTION))
        conways.updategrids()
        pygame.display.update()

if __name__ == '__main__':
    update(screen)