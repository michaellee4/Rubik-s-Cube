from constants import *
import pygame
import random
"""
Cube layed out as follows
              ----------------
               | 0  | 1  | 2  |
               ----------------
               | 3  | U  | 5  |
               ----------------
               | 6  | 7  | 8  |  
               ----------------  
-------------------------------------------------------------
| 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
-------------------------------------------------------------
| 12 |  L | 14 | 21 |  F | 23 | 30 |  R | 32 | 39 |  B | 41 |
-------------------------------------------------------------
| 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
-------------------------------------------------------------
               ----------------
               | 45 | 46 | 47 |
               ----------------
               | 48 |  D | 50 |
               ----------------
               | 51 | 52 | 53 |
               ----------------
"""


class Cube:
    def __init__(self):
        # self.faces = [[color for _ in range(kCubiesPerFace)] for color in Color]
        self.faces = [[random.choice(list(Color)) for _ in range(9)] for _ in range(kNumFaces)]
    
    def reset(self):
        self.faces = [[color for _ in range(kCubiesPerFace)] for color in Color]
    
    def draw(self, PyGameDisplay):
        for face in Face:
            # 150 and 200 are to center the drawing
            rowOff = row[face.value] * kCubeDim * kCubieSize + 150
            colOff = col[face.value] * kCubeDim * kCubieSize + 200
            for i in range(kCubiesPerFace):
                x = ((i %  kCubeDim) * kCubieSize) + colOff 
                y = ((i // kCubeDim) * kCubieSize) + rowOff
                color = self.faces[face.value][i].value
                pygame.draw.rect(PyGameDisplay, color, (x, y, kCubieSize, kCubieSize))
    def _rotateFaceMain(self, face):
        # rotate central face clockwise
        centralFace = self.faces[keyToFace[face].value]
        prevCC, prevEC = centralFace[corners[0]], centralFace[edges[0]]
        for i in range(1, len(corners)):
            centralFace[corners[i]], prevCC = prevCC, centralFace[corners[i]] 
            centralFace[edges[i]], prevEC = prevEC, centralFace[edges[i]] 

    def _rotateFaceSides(self, face):
        pass
        
    def rotateFace(self, face):
        self._rotateFaceMain(face)
        # get ordering of neighboring faces swap layers of kCubiesPerFace

