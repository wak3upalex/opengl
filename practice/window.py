import glfw
from OpenGL.GL import *

if not glfw.init():
    raise Exception("Error during Initialization")

# glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
# glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
# glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
# glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)  # Для macOS

window = glfw.create_window(2560, 1600, 'Based window', None, None)
if not window:
    glfw.terminate()
    raise Exception('Error creating a window')

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()