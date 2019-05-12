from pyglet.gl import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window()
#window.fullscreen=True

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, width / float(height), .1, 1000)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

pyglet.app.run()

print(window.__dict__)

for key,value in zip(window.__dict__.keys(),window.__dict__.values()):
    print(key,":",value)
