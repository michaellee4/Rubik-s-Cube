from enum import Enum
import pygame
# Layout based on https://ruwix.com/twisty-puzzles/bandaged-cube-puzzles/

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
    Face.F : [(6, 7, 8), (27, 30, 33), (47, 46, 45), (17, 14, 11), (6, 7, 8)],
    Face.R : [(2, 5, 8), (42, 39, 36), (47, 50, 53), (20, 23, 26), (2, 5, 8)],
    Face.B : [(29, 32, 35), (0, 1, 2), (15, 12, 9), (53, 52, 51), (29, 32, 35)],
    Face.D : [(24, 25, 26), (33, 34, 35), (42, 43, 44), (15, 16, 17), (24, 25, 26)]
}

strToFace = {
    'u' : Face.U,
    'l' : Face.L,
    'f' : Face.F,
    'r' : Face.R,
    'b' : Face.B,
    'd' : Face.D,

    'U' : Face.U,
    'L' : Face.L,
    'F' : Face.F,
    'R' : Face.R,
    'B' : Face.B,
    'D' : Face.D,

    'u2' : Face.U,
    'l2' : Face.L,
    'f2' : Face.F,
    'r2' : Face.R,
    'b2' : Face.B,
    'd2' : Face.D,

    'U2' : Face.U,
    'L2' : Face.L,
    'F2' : Face.F,
    'R2' : Face.R,
    'B2' : Face.B,
    'D2' : Face.D,

    'u\'' : Face.U,
    'l\'' : Face.L,
    'f\'' : Face.F,
    'r\'' : Face.R,
    'b\'' : Face.B,
    'd\'' : Face.D,

    'U\'' : Face.U,
    'L\'' : Face.L,
    'F\'' : Face.F,
    'R\'' : Face.R,
    'B\'' : Face.B,
    'D\'' : Face.D
}

# Stuff for Thistlewaite's
g0moves = { 'L', 'R', 'F', 'B', 'U', 'D'}
g1moves = { 'L', 'R', 'F', 'B', 'U2', 'D2' }
g2moves = { 'L', 'R', 'F2', 'B2', 'U2', 'D2' }
g3moves = { 'L2', 'R2', 'F2', 'B2', 'U2', 'D2' }