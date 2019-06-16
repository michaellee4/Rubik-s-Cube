from constants import *
import pygame
import random

"""
Cube layed out as a contiguous array as follows
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
        self.doneState = []
        for color in Color:
            self.doneState += [color for _ in range(kCubiesPerFace)]
        self.faces = self.doneState[:]
        # self.faces = [ random.choice(list(Color)) for _ in range(kNumFaces * kCubiesPerFace)]
    
    def reset(self):
        self.faces = self.doneState[:]

    def scramble(self):
        for _ in range(30):
            self.rotateFace(random.choice(turnKeys))
    
    def isSolved(self):
        return self.faces == self.doneState

    def draw(self, PyGameDisplay):
        for face in Face:
            # 150 and 200 are to center the drawing
            rowOff = row[face.value] * kCubeDim * kCubieSize + 150
            colOff = col[face.value] * kCubeDim * kCubieSize + 200
            for i in range(kCubiesPerFace):
                x = ((i %  kCubeDim) * kCubieSize) + colOff 
                y = ((i // kCubeDim) * kCubieSize) + rowOff
                color = self.faces[face.value * kCubiesPerFace + i].value
                pygame.draw.rect(PyGameDisplay, color, (x, y, kCubieSize, kCubieSize))
            
    def _rotateFaceMain(self, face):
        # rotate central face clockwise
        faceOff = face.value * kCubiesPerFace
        prevCC, prevEC = self.faces[faceOff + corners[0]], self.faces[faceOff + edges[0]]
        for i in range(1, len(corners)):
            self.faces[faceOff + corners[i]], prevCC = prevCC, self.faces[faceOff + corners[i]] 
            self.faces[faceOff + edges[i]], prevEC = prevEC, self.faces[faceOff + edges[i]] 

    def _rotateFaceSides(self, face):
        # get the sequence of swapped triples
        swaps = sidesToSwap[face]
        prevSideColors = [self.faces[s] for s in swaps[0]]
        for i in range(1, len(swaps)):
            curSideIdxs = swaps[i]
            for j in range(len(prevSideColors)):
                self.faces[curSideIdxs[j]], prevSideColors[j] = prevSideColors[j], self.faces[curSideIdxs[j]] 

    def rotateFace(self, face, numTurns = 1):
        for _ in range(numTurns):
            self._rotateFaceMain(face)
            self._rotateFaceSides(face)
        # get ordering of neighboring faces swap layers of kCubiesPerFace

    def performMoveSequence(self, moveList):
        for movestr in moveList:
            face, nTurns = strToFace[movestr]
            self.rotateFace(face, nTurns)

