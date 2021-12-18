from path_helpers import *
import numpy as np

# Breadth-first search algorithm
def bfs(screen, matrix, start, end):
    adjacent = []
    visited = []
    
    matrix[start] = 0
    matrix[end] = 2


    visited.append(start)
    append_adjacent(adjacent, visited, start)

    curr = start
    while adjacent != [] and curr != end:
        curr = adjacent.pop(0)
        if curr not in visited:
            visited.append(curr)
            matrix[curr] = 3
        
        append_adjacent(adjacent, visited, curr)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        draw_matrix(screen, matrix)
        pygame.display.flip()
                


