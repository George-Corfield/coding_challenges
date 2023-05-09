import random
import math


class Chaos:

    def __init__(self,height,width,n,rule=None):
        self.vertex = []
        self.rule = rule
        print(self.rule)
        self.n = n
        self.r = height//2 
        self.px = width//2
        self.py = height//2
        self.a = 2*math.pi/self.n
        for i in range(self.n):
            a = self.a*i
            colour1 = random.randint(0,255)
            colour2 = random.randint(0,255)
            colour3 = random.randint(0,255)
            self.vertex.append((self.px+(self.r*math.sin(a)),
            self.py-(self.r*math.cos(a)),(colour1,colour2,colour3)))
        self.start = (random.randint(0,width),random.randint(0,height))
        self.colour= (0,0,0)
        self.ref0 = [-1,-1,-1]
        self.current = self.start

    def create_point(self):
        self.ref = random.randint(0,self.n-1)
        if self.rule == 1:
            while self.ref == self.ref0[-1]:
                self.ref = random.randint(0,self.n-1)
        elif self.rule == 2:
            while (self.ref+self.n-1)%self.n == self.ref0[-1]:
                self.ref = random.randint(0,self.n-1)
        elif self.rule == 3:
            while (self.ref+2)%self.n == self.ref0[-1]:
                self.ref = random.randint(0,self.n-1)
        elif self.rule==4:
            while True:
                if (self.ref0[0] == self.ref0[1]) and ((self.ref+self.n-1)%self.n == self.ref0[-1] or (self.ref+self.n+1)%self.n == self.ref0[-1]):
                    self.ref = random.randint(0,self.n-1)
                else:
                    break

        else:
            pass
        self.x = (self.vertex[self.ref][0]+self.current[0])//2
        self.y = (self.vertex[self.ref][1]+self.current[1])//2
        self.colour = self.vertex[self.ref][2]
        self.current = (self.x,self.y)
        self.ref0.pop(0)
        self.ref0.append(self.ref)
        '''
        while (self.ref+2)%4 == self.ref0:
            self.ref = random.randint(0,3)
        if self.ref == 0:
            self.colour = (255,0,0)
            self.x = (self.A[0]+self.current[0])//2
            self.y = (self.A[1]+self.current[1])//2
        elif self.ref == 1:
            self.colour = (0,0,255)
            self.x = (self.B[0]+self.current[0])//2
            self.y = (self.B[1]+self.current[1])//2
        elif self.ref == 2:
            self.colour=(0,255,0)
            self.x = (self.C[0]+self.current[0])//2
            self.y = (self.C[1]+self.current[1])//2
        else:
            self.colour=(0,255,255)
            self.x = (self.D[0]+self.current[0])//2
            self.y = (self.D[1]+self.current[1])//2
        self.current = (self.x,self.y)
        self.ref0 = self.ref'''
        return self.current, self.colour


