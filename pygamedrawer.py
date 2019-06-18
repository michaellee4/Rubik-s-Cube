import pygame
from cube import Cube
from constants import *
import os
import sys

col = [1, 0, 1, 2, 3, 1]
row = [0, 1, 1, 1, 1, 2]
turnKeys = { pygame.K_u, pygame.K_l, pygame.K_f, pygame.K_r, pygame.K_b, pygame.K_d }

keyToFace = {
    pygame.K_u : Face.U,
    pygame.K_l : Face.L,
    pygame.K_f : Face.F,
    pygame.K_r : Face.R,
    pygame.K_b : Face.B,
    pygame.K_d : Face.D    
}

class PyGameCubeDrawer:
    def draw(self, cube, screen):
        for face in Face:
            # 150 and 200 are to center the drawing
            rowOff = row[face.value] * kCubeDim * kCubieSize + 150
            colOff = col[face.value] * kCubeDim * kCubieSize + 200
            for i in range(kCubiesPerFace):
                x = ((i %  kCubeDim) * kCubieSize) + colOff 
                y = ((i // kCubeDim) * kCubieSize) + rowOff
                color = cube.faces[face.value * kCubiesPerFace + i].value
                pygame.draw.rect(screen, color, (x, y, kCubieSize, kCubieSize))

class PyGameLoop:
    def init(self):
        # Pygame set-up
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption('Rubik\'s cube')
        self.screen = pygame.display.set_mode((kScreenWidth, kScreenHeight))
    
    def run(self):
        cube = Cube()
        cubeDrawer = PyGameCubeDrawer()
        shouldQuit = False
        while not shouldQuit:
            self.screen.fill((0, 0, 0))
            cubeDrawer.draw(cube, self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    shouldQuit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        shouldQuit = True
                    if event.key in turnKeys:
                        cube.rotateFace(keyToFace[event.key])
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            cube.rotateFace(keyToFace[event.key])
                            cube.rotateFace(keyToFace[event.key])
        pygame.quit()
        sys.exit()