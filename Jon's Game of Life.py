import sys, pygame
from tkinter.constants import Y
import numpy as np
import matplotlib.pyplot as plt
import time

pygame.init()

size = width, height = 600, 600

nxC = 60
nyC = 60

dimCW = (width - 1)  / nxC
dimCH = (height - 1) / nyC

bg = 25, 25, 25

screen = pygame.display.set_mode(size)

gameState = np.random.randint(0, 2, (nxC, nyC))

while 1:

    screen.fill(bg)

    new_gameState = np.copy(gameState)

    for y in range(0, nyC):
        for x in range(0, nxC):
            
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x)     % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y)     % nyC] + \
                      gameState[(x + 1) % nxC, (y)     % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x)     % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC]

            # A dead cell is "born" with exactly 3 living neighboring cells            
            if gameState[x, y] == 0 and n_neigh == 3:
                new_gameState[x, y] = 1
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                new_gameState[x, y] = 0

            poly = [((x - 1)* dimCW,  (y - 1) * dimCH),
                    ((x) * dimCW,     (y - 1) * dimCH),
                    ((x) * dimCW,     (y) * dimCH),
                    ((x - 1) * dimCW, (y) * dimCH)]

            pygame.draw.polygon(screen, (128, 28, 128), poly, int(abs(1- new_gameState[x, y]))) 

    gameState = new_gameState
    time.sleep(0.002)
    pygame.display.flip()