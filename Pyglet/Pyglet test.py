from pyglet.gl import *

class Model:
    def get_tex(self,file):
        tex=pyglet.image.load(file).texture
        glTexParameterf(Gl_TEXTURE_2D,L_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(Gl_TEXTURE_2D,L_TEXTURE_MIN_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self):

        self.top=self.get_tex("grass_top.png")
        self.size=self.get_tex("grass_side.png")
        self.bottom=self.get_tex("dirt.png")

        self.batch=pyglet.graphics.Batch()

        tex_coords=("t3f",(0,0,1,0,1,1,0,1))

        x,y,z=0,0,0
        X,Y,Z=x+1,y+1,z+1

        self.batch.add(4,GL_SQUADS,None,("v3f",(x,y,z,X,y,z,X,Y,z,x,Y,z)))

    def draw(self):
        self.batch.draw()

class Player:
    def __inint__(self):
        pass

    def update(self,dt,keys):
        if keys[key.A]: print("a")

class Window(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(300,200)

        self.model=Model()

    def Projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def Model(self):
        glMatrixMode(GL_MODELVIEW):
        glLoadIdentity()

    def set2d(self):
        gluOrthod
        self.Projection()
        self.


    def set3d(self):
        self.Projection()
        #persperctive
        self.Model()

    def on_draw(self):
        self.clear()
        self.set3d()
        self.Rotate()
        self.model.draw()

    def on_key_press(self,KEY,MOD):
        if KEY==key.ESCAPE: self.close()
        elif KEY==key.SPACE: self.mouse_lock= not self.mouse.lock

    def update(self,dt):
        self.player.update(dt,)


if __name__=="__main__":
    window=Window(width=400,height=300,caption="Awesome Game",resizable=True)
    glClearColor(0.5,0.7,1,1)
    pyglet.app.run()
