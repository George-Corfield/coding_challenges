import random

class Conways:
    def __init__(self,resolution,width,height):
        self.resolution = resolution
        self.height = height
        self.width = width
        self.rows = self.height//self.resolution
        self.cols = self.width//self.resolution
        self.cgrid,self.ngrid = self.make2Darray(self.cols,self.rows )
        self.counter = 1
        for i in range(self.rows):
            for j in range(self.cols):
                self.cgrid[i][j] = random.randint(0,1)

    def make2Darray(self,cols,rows):
        array1 = [[0 for i in range(cols)] for j in range(rows)]
        array2 = [[0 for i in range(cols)] for j in range(rows)]
        return array1, array2

    def updategrids(self):
        for i in range(self.rows):
            for j in range(self.cols):
                counter = self.countNeighbors(i,j)
                if (self.cgrid[i][j]==1 and (counter < 2 or counter >3)):
                    self.ngrid[i][j] = 0
                elif (self.cgrid[i][j] == 0 and counter == 3):
                    self.ngrid[i][j] = 1
                else:
                    self.ngrid[i][j] = self.cgrid[i][j]
        self.ngrid,self.cgrid = self.cgrid,self.ngrid


    def countNeighbors(self,x,y):
        counter = 0
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if i == 0 and j == 0:
                    continue
                else:
                    counter += self.cgrid[(x+i+self.rows)%self.rows][(y+j+self.cols)%self.cols]
        return counter


    



