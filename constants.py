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

turnKeys = { pygame.K_u, pygame.K_l, pygame.K_f, pygame.K_r, pygame.K_b, pygame.K_d }

keyToFace = {
    pygame.K_u : Face.U,
    pygame.K_l : Face.L,
    pygame.K_f : Face.F,
    pygame.K_r : Face.R,
    pygame.K_b : Face.B,
    pygame.K_d : Face.D    
}

sidesToSwap = {
    Face.U : [(9, 10, 11), (36, 37, 38), (27, 28, 29), (18, 19, 20), (9, 10, 11)],
    Face.L : [(0, 3, 6), (18, 21, 24), (45, 48, 51), (44, 41, 38), (0, 3, 6)],
    Face.F : [(6, 7, 8), (27, 30, 33), (45, 46, 47), (11, 14, 17), (6, 7, 8)],
    Face.R : [(2, 5, 8), (42, 39, 36), (47, 50, 53), (20, 23, 26), (2, 5, 8)],
    Face.B : [(29, 32, 35), (0, 1, 2), (15, 12, 9), (53, 52, 51), (29, 32, 35)],
    Face.D : [(24, 25, 26), (33, 34, 35), (42, 43, 44), (15, 16, 17), (24, 25, 26)]
}