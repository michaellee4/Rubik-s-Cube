from cube import Cube
import pygame
import os
import sys
from constants import *
import random

if __name__ == "__main__":
    c = Cube()

    # Pygame set-up
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Rubik\'s cube')
    screen = pygame.display.set_mode((kScreenWidth, kScreenHeight))
    fpsclock = pygame.time.Clock()

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
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    shouldQuit = True
                if event.key in turnKeys:
                    cube.performRotate(event.key)
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        cube.performRotate(event.key)
                        cube.performRotate(event.key)
    pygame.quit()
    sys.exit()