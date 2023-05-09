from numpy import array
import colorsys
import random

def rgb_conv(i):
    colour = 255 * array(colorsys.hsv_to_rgb(i/255.0,1.0,0.5))
    return tuple(colour.astype(int))

def rbg_conv(i):
    Scolour = colorsys.hsv_to_rgb(i/255,1,0.5)
    Ecolour = (int(x*255) for x in Scolour)
    return tuple(Ecolour)

if __name__ == '__main__':
    for i in range(10):
        x = random.randint(1,70)
        print(rgb_conv(x))
        print(rbg_conv(x))
