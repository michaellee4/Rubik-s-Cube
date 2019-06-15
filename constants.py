from enum import Enum
import pygame
# Based on https://ruwix.com/twisty-puzzles/bandaged-cube-puzzles/

class Color(Enum):
    YELLOW = (255, 213, 0)
    GREEN  = (0, 155, 72)
    ORANGE = (255, 89, 0)
    BLUE   = (0, 69, 173)
    RED    = (185, 0, 0)
    WHITE  = (255, 255, 255)

class Face(Enum):
    U      = 0
    L      = 1
    F      = 2
    R      = 3
    B      = 4
    D      = 5

kCubeDim = 3
kNumFaces = 6
kCubiesPerFace = kCubeDim * kCubeDim
kScreenWidth = 1080
kScreenHeight = 720
kCubieSize = 50

# Stuff for drawing
col = [1, 0, 1, 2, 3, 1]
row = [0, 1, 1, 1, 1, 2]
corners =   [0, 2, 8, 6, 0]
edges   =   [1, 5, 7, 3, 1]

keyToFace = {
    pygame.K_u : Face.U,
    pygame.K_l : Face.L,
    pygame.K_f : Face.F,
    pygame.K_r : Face.R,
    pygame.K_b : Face.B,
    pygame.K_d : Face.D    
}