from settings import *
import numpy as np
import pygame


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
    screen.fill(BLACK)
    for row in range(np.shape(matrix)[0]):
        for col in range(np.shape(matrix)[1]):
            node = matrix[row, col]
            if node == 0:
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, WHITE)
            else:
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, BLACK)
