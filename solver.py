from cube import Cube
from constants import *


# Stuff for Thistlewaite's
g0moves = { 'L', 'R', 'F', 'B', 'U', 'D'}
g1moves = { 'L', 'R', 'F', 'B', 'U2', 'D2' }
g2moves = { 'L', 'R', 'F2', 'B2', 'U2', 'D2' }
g3moves = { 'L2', 'R2', 'F2', 'B2', 'U2', 'D2' }


class Solver:
    def __init__(self):
        pass
        
    def solve(self, cube):
        moves = self.thistlewaite(cube)
        return moves

    def _thistlewaitePhase1(self, cube):
        def allEdgesGood(cube):
            return all(cube.faces[x] == x % 9 for x in edgeCubies)

        phase1_moves = []
        seen_states = set()
        def phase1_dfs(cur_depth):
            if allEdgesGood(cube):
                return True
            if cube.getHash() in seen_states:
                return False
            if cur_depth > 12:
                return False
            seen_states.add(cube.getHash())
            for move in g0moves:
                phase1_moves.append(move)
                cube.performMove(move)
                if phase1_dfs(cur_depth + 1):
                    return True
                cube.undoMove(move)
                phase1_moves.pop()
            return False
        phase1_dfs(0)
        return phase1_moves

    def _thistlewaitePhase2(self, cube):
        def allCornersGood(cube):
            return all(cube.corners[x] == x // kCubeDim for x in edgeCubies)

        phase2_moves = []
        seen_states = set()
        def phase2_dfs(cur_depth):
            if allCornersGood(cube):
                return True
            if cube.getHash() in seen_states:
                return False
            seen_states.add(cube.getHash())
            for move in g1moves:
                phase2_moves.append(move)
                cube.performMove(move)
                if phase2_dfs(cur_depth + 1):
                    return True
                cube.undoMove(move)
                phase2_moves.pop()
            return False
        phase2_dfs(0)
        return phase2_moves

    def _thistlewaitePhase3(self, cube):
        phase3_moves = []
        seen_states = set()

        def cornersPermuted(cube):
            return all(cube.faces[corner] == cube.doneState[corner] for corner in cornerCubies)
        
        def edgesPermuted(cube):
            return all(cube.faces[edge] == cube.doneState[edge] for edge in edgeCubies)

        def permuteEdges():
            if cornersPermuted(cube):
                return True
            if cube.getHash() in seen_states:
                return False
            seen_states.add(cube.getHash())
            for move in g2moves:
                phase3_moves.append(move)
                cube.performMove(move)
                if permuteEdges():
                    return True
                cube.undoMove(move)
                phase3_moves.pop()
            return False
            
        def permuteCorners():
            if edgesPermuted(cube):
                return True
            if cube.getHash() in seen_states:
                return False
            seen_states.add(cube.getHash())
            for move in g2moves:
                phase3_moves.append(move)
                cube.performMove(move)
                if permuteCorners():
                    return True
                cube.undoMove(move)
                phase3_moves.pop()
            return False


        permuteEdges()
        seen_states = set()
        permuteCorners()
        return phase3_moves

    def _thistlewaitePhase4(self, cube):
        phase4_moves = []
        seen_states = set()

        def finishCube():
            if cube.isSolved():
                return True
            hsh = cube.getHash()
            if hsh in seen_states:
                return False
            seen_states.add(hsh)
            for move in g3moves:
                phase4_moves.append(move)
                cube.performMove(move)
                if finishCube():
                    return True
                cube.undoMove(move)
                phase4_moves.pop()

        return phase4_moves

    def thistlewaite(self, cube):
        g1 = self._thistlewaitePhase1(cube)
        g2 = self._thistlewaitePhase2(cube)
        g3 = self._thistlewaitePhase3(cube)
        g4 = self._thistlewaitePhase4(cube)
        return g1 + g2 + g3 + g4