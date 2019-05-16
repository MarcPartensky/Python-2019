
import pyglet
window = pyglet.window.Window()
context = window.context
config = context.config
config.double_buffer
config.stereo
config.sample_buffers


platform = pyglet.window.get_platform()
