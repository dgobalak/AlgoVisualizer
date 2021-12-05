from settings import *
# from sorting_algos.selection_sort import *
import numpy as np
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

matrix = np.ones((NUM_ROWS, NUM_COLS))

ALGO = "SORT"   # Or "PATH"

# FOR TESTING
# matrix[-1] = np.zeros((len(matrix[0])))
# matrix[:, -1] = np.zeros((len(matrix[:, 0])))

def matrix_from_nums(nums, matrix):
    for col in range(np.shape(matrix)[1]):
        num = nums[col]
        tmp_col = np.ones(len(matrix[:, col]))
        tmp_col[(len(tmp_col)-num):(len(tmp_col))] = 0
        matrix[:, col] = tmp_col


def randomize_sorting_matrix(matrix):
    rand_nums = np.arange(1, NUM_COLS + 1, NUM_ROWS//NUM_COLS)
    np.random.shuffle(rand_nums)
    
    matrix_from_nums(rand_nums, matrix)
    
    return rand_nums


def draw_node(screen, x, y, color):
    pygame.draw.rect(screen, color, [x, y, NODE_WIDTH, NODE_HEIGHT])


def draw_matrix(screen, matrix):
    for row in range(np.shape(matrix)[0]):
        for col in range(np.shape(matrix)[1]):
            node = matrix[row, col]
            if node == 0:
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, WHITE)
            else:
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, BLACK)


def selection_sort(screen, matrix):
    nums = randomize_sorting_matrix(matrix)
    screen.fill(BLACK)
    clock.tick(FPS)  
    
    for i in range(len(nums)):
        screen.fill(BLACK)
        clock.tick(FPS)  
    
        min_i, min_val = i, nums[i]
        for j in range(i, len(nums)):
            if nums[j] <= min_val:
                min_i, min_val = j, nums[j]
        nums[i], nums[min_i] = nums[min_i], nums[i]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        matrix_from_nums(nums, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()    

selection_sort(screen, matrix)