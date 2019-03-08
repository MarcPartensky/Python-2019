from pyglet.gl import *
from Triangle import Triangle

class Window(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(400,300)
        glClearColor(0,0,1,1)

        self.triangle=Triangle()

    def on_draw(self):
        self.clear()
        glDrawArrays(GL_TRIANGLES,0,3)

    def on_resize(self,width,height):
        glViewport(0,0,width,height)

if __name__=="__main__":
    window=Window(700,600,"My awesome window",resizable=True)
    pyglet.app.run()
