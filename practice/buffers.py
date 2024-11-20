from OpenGL.GL import *
import numpy as np

def create_vao(vertices):
    """
    Creates a Vertex Array Object (VAO) and Vertex Buffer Object (VBO).

    """
    vertices = np.array(vertices, dtype=np.float32)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)