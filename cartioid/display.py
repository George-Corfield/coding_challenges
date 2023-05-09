import pygame
import sys
import math

height = width = 500
pygame.init()
pygame.display.set_caption('Cartioid')
screen = pygame.display.set_mode((width,height))
vertex = 200
centerx = centery = 250
radius = 230
clock = pygame.time.Clock()
fps = 60



def main():
    factor = 2
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(fps)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),(centerx,centery),radius,1)
        for i in range(vertex):
            vector = getVector(i,vertex,radius)
            pygame.draw.circle(screen,(255,255,255),vector,3)
        pygame.display.flip()
        for i in range(vertex):
            vectora = getVector(i,vertex,radius)
            vectorb = getVector(i*factor,vertex,radius)
            pygame.draw.line(screen,(255,255,255),vectora,vectorb,1)
        pygame.display.flip()
        factor+=0.01
        
        


def getVector(vertex, totalVertex,r):
    angle = (2*math.pi/totalVertex)*(vertex%totalVertex)
    vector = (centerx + r*math.sin(angle),centery + r*math.cos(angle))
    return vector

if __name__ == '__main__':
    main()