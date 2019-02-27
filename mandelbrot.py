from math import sqrt

class Mandelbrot:
    def __init__(self,size,zone):
        self.zone=zone
        self.generate(self.size,self.zone)
    def generate(self,zone):
        zx,zy,zmx,zmy=zone
        sx,sy=self.size
        self.grid=[[0 for i in range(sx)] for j in range(sy)]
        maximum=0
        zsx=zmx-zx
        zsy=zmy-zy
        for y in range(sy):
            for x in range(sy):
                X=zx+x*zsx/sx
                Y=zy+y*zsy/sy
                self.grid[y][x]=self.evaluate(X,Y)
                maximum=max(maximum,convergence)
        self.maximum=maximum

    def show(self,grid):
        
        color=self.percentToRGB(convergence/10)




    def evaluate(self,x,y,step=10):
        for i in range(step):
            a=x+x**2-y**2
            y=y+2*x*y
            x=a
        value=sqrt(x**2+y**2)

    def percentToRGB(self,percentage):
        wavelength=percentage*400+380
        gamma,max_intensity=0.80,255
        def adjust(color, factor):
            if color==0: return 0
            else: return round(max_intensity*pow(color*factor,gamma))
        if 380<=wavelength<=440: r,g,b=-(wavelength-440)/(440-380),0,1
        elif 440<=wavelength<=490: r,g,b=0,(wavelength-440)/(490-440),1
        elif 490<=wavelength<=510: r,g,b=0,1,-(wavelength-510)/(510-490)
        elif 510<=wavelength<=580: r,g,b=(wavelength-510)/(580-510),1,0
        elif 580<=wavelength<=645: r,g,b=1,-(wavelength-645)/(645-580),0
        elif 645<=wavelength<=780: r,g,b=1,0,0
        else: r,g,b=0,0,0
        if 380<=wavelength<=420: factor=0.3+0.7*(wavelength-380)/(420-380)
        elif 420<=wavelength<=701: factor=1
        elif 701<=wavelength<=780: factor=0.3+0.7*(780-wavelength)/(780-700)
        else: factor=0
        r,g,b=adjust(r,factor),adjust(g,factor),adjust(b,factor)
        return (r,g,b)
