from settings import *
import numpy as np
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

matrix = np.ones((NUM_ROWS, NUM_COLS))

# FOR TESTING
# matrix[-1] = np.zeros((len(matrix[0])))
# matrix[:, -1] = np.zeros((len(matrix[:, 0])))

def randomize_sorting_matrix(matrix):
    rand_nums = np.arange(1, NUM_COLS + 1, NUM_ROWS//NUM_COLS)
    np.random.shuffle(rand_nums)
    
    for col in range(np.shape(matrix)[1]):
        rand_num = rand_nums[col]
        tmp_col = np.ones(len(matrix[:, col]))
        tmp_col[(len(tmp_col)-rand_num):(len(tmp_col))] = 0
        matrix[:, col] = tmp_col


def create_square(x, y, color):
    pygame.draw.rect(screen, color, [x, y, NODE_WIDTH, NODE_HEIGHT])


randomize_sorting_matrix(matrix)
print(list(matrix))
## Game loop
running = True
while running:
    screen.fill(BLACK)
    clock.tick(FPS)   
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for row in range(np.shape(matrix)[0]):
        for col in range(np.shape(matrix)[1]):
            node = matrix[row, col]
            if node == 0:
                create_square(col*NODE_WIDTH, row*NODE_HEIGHT, WHITE)
            else:
                create_square(col*NODE_WIDTH, row*NODE_HEIGHT, BLACK)

    pygame.display.flip()       

