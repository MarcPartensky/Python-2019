
import pyglet
window = pyglet.window.Window()
context = window.context
config = context.config
config.double_buffer
config.stereo
config.sample_buffers


platform = pyglet.window.get_platform()
display = platform.get_default_display()

for screen in display.get_screens():
    print(screen)
