from pyglet.gl import *
from pyglet.window import key
import math
from main import Model


class Model2(Model):

    def get_tex(self,file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self):

        self.top = self.get_tex('grass_top.png')
        self.side = self.get_tex('grass_side.png')
        self.bottom = self.get_tex('dirt.png')

        self.batch = pyglet.graphics.Batch()

        tex_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))


        for zi in range(-10,10):
            for yi in range(-10,10):
                for xi in range(-10,10):
                    self.addCube(xi,yi,zi)


        yi=-10
        for zi in range(-100,100):
            for xi in range(-100,100):
                self.addCube(xi,yi,zi)

    def addCube(self,xi,yi,zi):
        x,y,z = xi,yi,zi-1
        X,Y,Z = x+1,y+1,z+1

        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.side,('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.bottom,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.top,('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.side,('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),tex_coords)
        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),tex_coords)


    def draw(self):
        self.batch.draw()

class Player:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def mouse_motion(self,dx,dy):
        dx/=8; dy/=8; self.rot[0]+=dy; self.rot[1]-=dx
        if self.rot[0]>90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def update(self,dt,keys):
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        if keys[key.W]: self.pos[0]+=dx; self.pos[2]-=dz
        if keys[key.S]: self.pos[0]-=dx; self.pos[2]+=dz
        if keys[key.A]: self.pos[0]-=dz; self.pos[2]-=dx
        if keys[key.D]: self.pos[0]+=dz; self.pos[2]+=dx

        if keys[key.SPACE]: self.pos[1]+=s
        if keys[key.LSHIFT]: self.pos[1]-=s


class Window(pyglet.window.Window):

    def push(self,pos,rot): glPushMatrix(); glRotatef(-rot[0],1,0,0); glRotatef(-rot[1],0,1,0); glTranslatef(-pos[0],-pos[1],-pos[2],)
    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def set2d(self): self.Projection(); gluOrtho2D(0,self.width,0,self.height); self.Model()
    def set3d(self): self.Projection(); gluPerspective(70,self.width/self.height,0.05,1000); self.Model()

    def setLock(self,state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self,*args,**kwargs):
        """Create pyglet window."""
        super().__init__(*args,**kwargs)
        self.set_minimum_size(300,200)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.model=Model2()
        self.player=Player((0.5,1.5,1.5),(-30,0))

    def on_mouse_motion(self,x,y,dx,dy):
        """Set the parameters of the view of the player using the position of the mouse."""
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        """Determine if the window must be closed."""
        if KEY == key.ESCAPE: self.close()
        #elif KEY == key.E: self.mouse_lock = not self.mouse_lock
        self.mouse_lock=True

    def update(self,dt):
        """Update the player's view using time dt and knowning keys."""
        self.player.update(dt,self.keys)

    def on_draw(self):
        """Overload function automatically called by the pyglet window while running."""
        self.clear()
        self.set3d()
        self.push(self.player.pos,self.player.rot)
        self.model.draw()
        glPopMatrix()


if __name__ == '__main__':
    window = Window(width=1440,height=900,caption='Minecraft',fullscreen=True)
    r,g,b,alpha=0,0,0,1 #Color of the background and transparency alpha, each component's value must be between 0 and 1
    glClearColor(r,g,b,alpha) #Apply the background
    #glEnable allows to change the parameters of the opengl interface
    glEnable(GL_DEPTH_TEST) #Allow the objects not to be displayed when behing others, must be enabled to prevent weird bugs
    #glEnable(GL_CULL_FACE)
    pyglet.app.run()
