from cube import Cube
from constants import *


# Stuff for Thistlewaite's
g0moves = { 'L', 'R', 'F', 'B', 'U', 'D'}
g1moves = { 'L', 'R', 'F', 'B', 'U2', 'D2' }
g2moves = { 'L', 'R', 'F2', 'B2', 'U2', 'D2' }
g3moves = { 'L2', 'R2', 'F2', 'B2', 'U2', 'D2' }

class Solver:
    def __init__(self):
        self.moves = []
        

    def solve(self, cube):
        self.thistlewaite(cube)
        return self.moves

    def _thistlewaitePhase1(self, cube):
        return []

    def _thistlewaitePhase2(self, cube):
        return []

    def _thistlewaitePhase3(self, cube):
        return []

    def _thistlewaitePhase4(self, cube):
        return []

    def thistlewaite(self, cube):
        g1 = self._thistlewaitePhase1(cube)
        g2 = self._thistlewaitePhase2(cube)
        g3 = self._thistlewaitePhase3(cube)
        g4 = self._thistlewaitePhase4(cube)
        self.moves = g1 + g2 + g3 + g4