import pygame
import random
from pygame.locals import *
from constants import *
from cube import Cube

from OpenGL.GL import *
from OpenGL.GLU import *
# https://stackoverflow.com/questions/50303616/how-to-rotate-slices-of-a-rubiks-cube-in-python-pyopengl

vertices = (
    ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1), (-1, -1, -1),
    ( 1, -1,  1), ( 1,  1,  1), (-1, -1,  1), (-1,  1,  1)
)
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))
colors = (
    (185 / 255, 0, 0), #Red
    (0, 155 / 255, 72 / 255), #Green
    (255 / 255, 89 / 255, 0), #Orange
    (0, 69 / 255, 173 / 255), #Blue
    (255 / 255, 213 / 255, 0), #Yellow
    (1,1,1), #White
    )

rot_cube_map  = { K_UP: (-1, 0), K_DOWN: (1, 0), K_LEFT: (0, -1), K_RIGHT: (0, 1)}
rot_slice_map = {
    K_l: (0, 0, 1), K_r: (0, 2, -1), K_d: (1, 0, 1),
    K_u: (1, 2, -1), K_b: (2, 0, 1), K_f:  (2, 2, -1) 
}  
p_rot_slice_map = {
    K_l: (0, 0, -1), K_r: (0, 2, 1), K_d: (1, 0, -1),
    K_u: (1, 2, 1), K_b: (2, 0, -1), K_f: (2, 2, 1)
}  
    
class GLCubie():
    def __init__(self, id, scale):
        self.scale = scale
        self.init_i = [*id]
        self.current_i = [*id]
        self.rot = [[1 if i==j else 0 for i in range(3)] for j in range(3)]

    def isAffected(self, axis, slice, dir):
        return self.current_i[axis] == slice

    def update(self, axis, slice, dir):

        if not self.isAffected(axis, slice, dir):
            return

        i, j = (axis+1) % 3, (axis+2) % 3
        for k in range(3):
            self.rot[k][i], self.rot[k][j] = -self.rot[k][j]*dir, self.rot[k][i]*dir

        self.current_i[i], self.current_i[j] = (
            self.current_i[j] if dir < 0 else kCubeDim - 1 - self.current_i[j],
            self.current_i[i] if dir > 0 else kCubeDim - 1 - self.current_i[i] )

    def transformMat(self):
        scaleA = [[s*self.scale for s in a] for a in self.rot]  
        scaleT = [(p-(kCubeDim-1)/2)*2.1*self.scale for p in self.current_i] 
        return [*scaleA[0], 0, *scaleA[1], 0, *scaleA[2], 0, *scaleT, 1]

    def draw(self, col, surf, vert, animate, angle, axis, slice, dir):

        glPushMatrix()
        if animate and self.isAffected(axis, slice, dir):
            glRotatef( angle*dir, *[1 if i==axis else 0 for i in range(3)] )
        glMultMatrixf( self.transformMat() )

        glBegin(GL_QUADS)
        for i in range(len(surf)):
            glColor3fv(colors[i])
            for j in surf[i]:
                glVertex3fv(vertices[j])
        glEnd()

        glPopMatrix()

class GLCube():
    def __init__(self, flat_cube):
        cr = range(kCubeDim)
        self.gl_cubies = [GLCubie((x, y, z), 1.5) for x in cr for y in cr for z in cr]
        self.cube = flat_cube


class PyOpenGlLoop:

    def init(self, flat_cube):
        # OpenGL boilerplate
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        glEnable(GL_DEPTH_TEST) 
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        self.gl_cube = GLCube(flat_cube)
    
    def loop(self):
        ang_x, ang_y, rot_cube = 0, 0, (0, 0)
        animate, animate_ang, animate_speed = False, 0, 5
        action = (0, 0, 0)

        shouldQuit = False
        while not shouldQuit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    shouldQuit = True
                if event.type == KEYDOWN:

                    #Begin Rotate Camera
                    if event.key in rot_cube_map:
                        rot_cube = rot_cube_map[event.key]
                    
                    # Non-Prime Move
                    if not animate and event.key in rot_slice_map and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        animate, action = True, rot_slice_map[event.key]
                    
                    # Prime Move
                    elif not animate and event.key in p_rot_slice_map:
                        animate, action = True, p_rot_slice_map[event.key]
                
                # End Rotate Camera
                if event.type == KEYUP:
                    if event.key in rot_cube_map:
                        rot_cube = (0, 0)

            # Calculate new Angle for Camera
            ang_x += rot_cube[0]*2
            ang_y += rot_cube[1]*2

            # Perform Camera Translation
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glTranslatef(0, 0, -40)
            glRotatef(ang_y, 0, 1, 0)
            glRotatef(ang_x, 1, 0, 0)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            if animate:
                if animate_ang >= 90:
                    for cube in self.gl_cube.gl_cubies:
                        cube.update(*action)
                    animate, animate_ang = False, 0

            for cube in self.gl_cube.gl_cubies:
                cube.draw(colors, surfaces, vertices, animate, animate_ang, *action)
            if animate:
                animate_ang += animate_speed

            pygame.display.flip()
            pygame.time.wait(10)
        pygame.quit()
        sys.exit()

def main():
    flat_cube = Cube()
    flat_cube.scramble()
    loop = PyOpenGlLoop()
    loop.init(flat_cube)
    loop.loop()

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()