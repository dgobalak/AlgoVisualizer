from path_finding.path_helpers import *
import numpy as np


VISITED = 3


def dijkstra(screen, graph, start, end):
    visited_nodes = []
    costs = {}  # dict of nodes and their cost
    paths = {}   # dict of nodes and their shortest paths
    # All paths will begin at start and end on the desired node

    screen_matrix = graph.copy()
    screen_matrix[start] = 0
    screen_matrix[end] = 2

    # Set the starting cost and path for each node
    for x in range(np.shape(graph)[0]):
        for y in range(np.shape(graph)[1]):
            paths[(x, y)] = []
            if (x, y) == start:
                costs[(x, y)] = 0
                continue
            costs[(x, y)] = np.inf

    paths[start].append(start)

    while len(visited_nodes) < np.prod(np.shape(graph)):
        vertex = find_min(costs, visited_nodes)
        visited_nodes.append(vertex)

        if vertex != start and vertex != end:
            screen_matrix[vertex] = VISITED

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_matrix(screen, screen_matrix)
        pygame.display.flip()

        adjacent_nodes = get_adjacent(vertex)
        update_distances(graph, costs, vertex, adjacent_nodes, paths)

        if vertex == end:
            break

    for node in paths[end][1:-1]:
        screen_matrix[node] = 4

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_matrix(screen, screen_matrix)
        pygame.display.flip()


def find_min(costs, visited_nodes):
    min_node = None
    min_cost = np.inf

    for node, cost in costs.items():
        if node not in visited_nodes:
            if cost < min_cost:
                min_cost = cost
                min_node = node

    return min_node


def update_distances(graph, costs, curr, adjacent_nodes, paths):
    for node in adjacent_nodes:
        if costs[curr] + graph[node] < costs[node]:
            # Update shortest path score
            costs[node] = costs[curr] + graph[node]

            # Update shortest path of nodes
            tmp_path = paths[curr].copy()
            tmp_path.append(node)
            paths[node] = tmp_path
