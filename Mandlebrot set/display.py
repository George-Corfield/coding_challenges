import pygame
import colorsys
import sys

HEIGHT = 800
WIDTH = 1200
max_width = WIDTH
min_width =  0
max_height = HEIGHT
min_height = 0
iterations = 100
pygame.init()
pygame.display.set_caption('The Mandelbrot Set')
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def rgb_conv(i):
    Scolour = colorsys.hsv_to_rgb(i/360,1,1)
    Ecolour = (int(x*255) for x in Scolour)
    return tuple(Ecolour)

def update():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        for x in range(0,WIDTH):
            for y in range(0,HEIGHT):
                a = (((x-min_width)/(max_width-min_width))*3 - 2) #((OldVal - OldMin)/(OldMax-OldMin))*(NewMax - NewMin) - NewMin
                b = (((y-min_height)/(max_height-min_height))*2 - 1)
                ca,cb = a,b
                iteration = 0
                while iteration<iterations:
                    fa = a*a - b*b
                    fb = 2*a*b
                    a = fa + ca
                    b = fb + cb
                    if (a*a + b*b) > 4:
                        break
                    iteration+=1
                if iteration == iterations:
                    colour = (0,0,0)
                else:
                    colour = rgb_conv(iteration)
                screen.set_at((x,y),colour)
        pygame.display.update()


if __name__=='__main__':
    update()
