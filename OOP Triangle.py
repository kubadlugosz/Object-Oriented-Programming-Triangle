

import math
class Triangle(object):

    def __init__(self,Ax,Ay,Bx,By,Cx,Cy):
        self.x0 = Ax
        self.y0 = Ay
        self.x1 = Bx
        self.y1 = By
        self.x2 = Cx
        self.y2 = Cy
    def __str__(self):
        return "Triangle Points(%s,%s)(%s,%s)(%s,%s)" %(self.x0,self.y0,self.x1,self.y1,self.x2,self.y2)

    def area(self):
        return abs((1/2)*(self.x0*(self.y1-self.y2)+self.x1*(self.y2-self.y0)+self.x2*(self.y0-self.y1)))

    def perimeter(self):
        line1 = abs(math.sqrt(((self.x1-self.x0)**2)+(self.y1-self.y0)**2))
        line2 = abs(math.sqrt(((self.x2-self.x1)**2)+(self.y2-self.y1)**2))
        line3 = abs(math.sqrt(((self.x2-self.x0)**2+(self.y2-self.y0)**2)))
        return line1+line2+line3
        
    def baycenter(self):
        return (((self.x0+self.x1+self.x2)/3),((self.y0+self.y1+self.y2)/3))

    def Longest_side(self):
        line1 = abs(math.sqrt(((self.x1-self.x0)**2)+(self.y1-self.y2)**2))
        line2 = abs(math.sqrt(((self.x2-self.x1)**2)+(self.y2-self.y1)**2))
        line3 = abs(math.sqrt(((self.x2-self.x0)**2+(self.y2-self.y0)**2)))
        return max(line1,line2,line3)   

    def IsRightTriangle(self):
        e = 0.000000001
        line1 = abs(math.sqrt(((self.x1-self.x0)**2)+(self.y1-self.y2)**2))
        line2 = abs(math.sqrt(((self.x2-self.x1)**2)+(self.y2-self.y1)**2))
        line3 = abs(math.sqrt(((self.x2-self.x0)**2)+(self.y2-self.y0)**2))
        if abs(line1**2+line2**2-line3**2)< e:
            return True
        elif abs(line1**2+line3**2-line2**2)< e:
            return True
        elif abs(line2**2+line3**2-line1**2)< e:
            return True
        else:
            return False
        
        
       
def main():
   
    Triangle_Points=Triangle(3,-5,15,4,-6,10)
    print(Triangle_Points)
    print(Triangle_Points.area())
    print(Triangle_Points.perimeter())
    print(Triangle_Points.baycenter())
    print(Triangle_Points.Longest_side())
    print(Triangle_Points.IsRightTriangle())
    
    
main()
