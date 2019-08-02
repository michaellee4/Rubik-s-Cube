# Rubik's Cube

A fully interactive, 3D Rubik's Cube

## How to run
To use the engine in console mode on linux
1. Clone the repository
2. Make sure that 'loop = PyOpenGlLoop()' is set in main.py
3. Run the program using 'python3 main.py'

## Controls
* Up/Down/Left/Right - Controls the camera

* u/d/l/r/f/b - Performs a cube rotation based on the standard notation https://ruwix.com/the-rubiks-cube/notation/

* Shift + u/d/l/r/f/b - Performs an inverse cube rotation based on the standard notation

## Notes
* Currently, the solver is not fully working. Eventually this will implement Thistlewaite's algorithm which guarantees a solve in under 52 moves.
