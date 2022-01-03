from path_finding import *

import numpy as np
import pygame


def draw_node(screen, x, y, color):
    pygame.draw.rect(screen, color, [x, y, NODE_WIDTH, NODE_HEIGHT])


def draw_matrix(screen, matrix):
    screen.fill(BLACK)
    for row in range(np.shape(matrix)[0]):
        for col in range(np.shape(matrix)[1]):
            node = matrix[row, col]
            if node == 0:   # Start
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, GREEN)
            elif node == 2:  # End
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, RED)
            elif node == 3:  # Visited
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, BLUE)
            elif node == 4:
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, YELLOW)
            else:   # Board
                draw_node(screen, col*NODE_WIDTH, row*NODE_HEIGHT, BLACK)


def append_adjacent(adjacent, visited, node):
    # Append the 4 surrounding nodes
    temp_nodes = [left(node), right(node), below(node), above(node)]

    for adjacent_node in temp_nodes:
        if within_bounds(adjacent_node) and adjacent_node not in visited:
            if adjacent_node in adjacent:
                adjacent.remove(adjacent_node)
            adjacent.append(adjacent_node)


def get_adjacent(node):
    # Append the 4 surrounding nodes
    temp_nodes = [left(node), right(node), below(node), above(node), top_left(
        node), top_right(node), bottom_right(node), bottom_left(node)]
    adjacent = []

    for adjacent_node in temp_nodes:
        if within_bounds(adjacent_node):
            adjacent.append(adjacent_node)

    return adjacent


def within_bounds(node):
    if node[0] >= 0 and node[0] < SCREEN_WIDTH//NODE_WIDTH:
        if node[1] >= 0 and node[1] < SCREEN_HEIGHT//NODE_HEIGHT:
            return True
    return False


def add(a, b):
    return tuple(sum(x) for x in zip(a, b))


def above(coord):
    return add(coord, (0, 1))


def below(coord):
    return add(coord, (0, -1))


def left(coord):
    return add(coord, (-1, 0))


def right(coord):
    return add(coord, (1, 0))


def top_left(coord):
    return add(coord, (-1, 1))


def bottom_left(coord):
    return add(coord, (-1, -1))


def top_right(coord):
    return add(coord, (1, 1))


def bottom_right(coord):
    return add(coord, (1, -1))
