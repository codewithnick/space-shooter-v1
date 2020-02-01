class Bullet:
    def __init__(self,x,y):
        self.bulletx=x
        self.bullety=y
        self.bulletsizex=9
        self.bulletsizey=33
    def move(self):
        if self.bullety>0:
            self.bullety-=1
            
            
class Meteor:
    def __init__(self,x,y):
        self.meteorx=x
        self.meteory=y
        self.meteorhits=False
        self.smallmeteorrange=list(i for i in range(self.meteorx,self.meteorx+44))
        self.bigmeteorrange=list(i for i in range(self.meteorx,self.meteorx+136))
    def move(self):
        if self.meteory>0:
            self.meteory-=1
        
