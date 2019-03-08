from pyglet.gl import *
import pyglet



class Triangle:
    def __init__(self):
        self.vertices=pyglet.graphics.vertex_list(3,("v3f",[-0.5,-0.5,0.,0.5,-0.5,0.,0.,0.,0.5]),
                                                      ("c3B",[100,200,220,200,110,100,100,250,100]))


class Quad:
    def __init__(self):
        self.vertices=pyglet.graphics.vertex_list_indexed(4,[0,1,2,3,0],
                                                           ("v3f",[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]),
                                                           ("c3f",[0,1,0, 1,1,0, 1,0,0, 1,0,1]))

class Quad2:
    def __init__(self):
        self.indices=[0,1,2,3,0]
        self.vertex=[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
        self.color=[0,1,0, 1,1,0, 1,0,0, 1,0,1]
        self.vertices=pyglet.graphics.vertex_list_indexed(4,self.indices,("v3f",self.vertex),("c3f",self.color))

class Quad3:
    def __init__(self):
        self.indices=[0,1,2,3,0]
        self.vertex=[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
        self.color=[0,1,0, 1,1,0, 1,0,0, 1,0,1]

    def render(self):
        self.vertices=pyglet.graphics.draw_indexed(4,GL_TRIANGLES,self.indices,("v3f",self.vertex),("c3f",self.color))


class Window(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(400,300)
        color=(255,0,0)
        glClearColor(255,0,0,1.0)
        self.triangle=Triangle()
        self.quad=Quad3()

    def on_draw(self):
        self.clear()
        #self.triangle.vertices.draw(GL_TRIANGLES)
        #self.quad.vertices.draw(GL_QUADS)
        self.quad.render()

    def on_resize(self,width,height):
        glViewport(0,0,width,height)

if __name__=="__main__":
    window=Window(1280,720,"First Pyglet Window",resizable=True)
    pyglet.app.run()
