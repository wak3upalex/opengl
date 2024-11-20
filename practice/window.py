import glfw


def initialize_window(width, height, title):
    """
    Initializes window GLFW and create a GLFW window
    :param width: window width
    :param height: window height
    :param title: window title
    """
    if not glfw.init():
        raise Exception("Error during Initialization")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)  # Для macOS

    window = glfw.create_window(width, height, title, None, None)
    if not window:
        glfw.terminate()
        raise Exception('Error creating a window')

    glfw.make_context_current(window)
    return window


def terminate_window():
    """Terminates GLFW"""
    glfw.terminate()
