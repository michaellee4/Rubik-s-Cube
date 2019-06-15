from cube import Cube
import pygame
import os
import sys
from constants import *

if __name__ == "__main__":
    c = Cube()

    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Rubik\'s cube')
    screen = pygame.display.set_mode((kScreenWidth, kScreenHeight))
    fpsclock = pygame.time.Clock()
    ##tile size and margin size should add up to 120
    cube = Cube()
    shouldQuit = False
    while not shouldQuit:
        screen.fill((0, 0, 0))
        cube.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shouldQuit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    shouldQuit = True
                if event.key == pygame.K_u:
                    cube.rotateFace(event.key)
                if event.key == pygame.K_r:
                    cube.rotateFace(event.key)
                if event.key == pygame.K_l:
                    cube.rotateFace(event.key)
                if event.key == pygame.K_d:
                    cube.rotateFace(event.key)
                if event.key == pygame.K_b:
                    cube.rotateFace(event.key)
                if event.key == pygame.K_f:
                    cube.rotateFace(event.key)

        # program.update()
    pygame.quit()
    sys.exit()