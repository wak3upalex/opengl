import glfw
from OpenGL.GL import *
from window import initialize_window, terminate_window

def main():
    # Initialize window
    window = initialize_window(2560, 1600, "OpenGL Practice")

    vertices = [
        # Each vertex has an x, y, z coordinate
        -125 + 40, -125 + 30, -125,
        125 + 40, -125 + 30, -125,
        125 + 40, 125 + 30, -125,
        -125 + 40, 125 + 30, -125,
        -125 + 40, -125 + 30, 125,
        125 + 40, -125 + 30, 125,
        125 + 40, 125 + 30, 125,
        -125 + 40, 125 + 30, 125,
    ]

    # Main render loop
    while not glfw.window_should_close(window):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Swap buffers and poll events
        glfw.swap_buffers(window)
        glfw.poll_events()

    # Terminate GLFW
    terminate_window()

if __name__ == "__main__":
    main()
