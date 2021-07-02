import sys, pygame
from tkinter.constants import Y
import numpy as np
import matplotlib.pyplot as plt

pygame.init()

size = width, height = 600, 600

nxC = 60
nyC = 60

dimCW = (width - 1)  / nxC
dimCH = (height - 1) / nyC

bg = 25, 25, 25

# screen = pygame.display.set_mode(size)

# screen.fill(bg)

gameState = np.random.randint(0, 2, (nxC, nyC))

print(gameState)


while 1:
    
    for y in range(1, nyC + 1):
        for x in range(1, nxC + 1):
            
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x) % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y) % nyC] + \
                      gameState[(x + 1) % nxC, (y) % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x) % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC]

            print(n_neigh)


            #Una célula muerta con exactamente 3 celulas vecinas vivas "nace"
            np.sum(gameState[x-1 : x + 1, y-1 : y + 2]) - gameState[x, y]



            #Una célula viva con 2 0 3 células vecinas vivas sigue viva, en otro caso muere

            poly = [((y - 1)* dimCW,  (x - 1) * dimCH),
                    ((y) * dimCW,     (x - 1) * dimCH),
                    ((y)* dimCW,      (x) * dimCH),
                    ((y - 1)* dimCW,  (x) * dimCH)]
            
            
            plt.matshow(gameState)
            plt.show()

            #pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    
    #pygame.display.flip()