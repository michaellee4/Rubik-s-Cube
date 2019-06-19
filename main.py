from pygamedrawer import PyGameLoop
from pyopengldrawer import PyOpenGlLoop
from cube import Cube

if __name__ == "__main__":
    flat_cube = Cube()
    # flat_cube.scramble()
    loop = PyOpenGlLoop()
    loop.init(flat_cube)
    loop.run()
