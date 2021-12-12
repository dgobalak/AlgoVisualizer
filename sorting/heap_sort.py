from sorting_helpers import *
import pygame
import sys
import numpy as np
from copy import deepcopy


class Heap:
    ROOT_INDEX = 0
    LAST_INDEX = -1

    def __init__(self):
        self.heap = []
        self.size = 0

    def add(self, val):
        self.heap.append(val)

        i = self.size
        inPlace = False

        while i >= 0 and not inPlace:
            pi = self.parent_index(i)
            if pi < 0 or self.heap[pi] >= self.heap[i]:
                inPlace = True
            else:
                self.swap(pi, i)
                i = pi

        self.size += 1

    def pop_root(self):
        val = self.heap[self.ROOT_INDEX]
        self.swap(self.ROOT_INDEX, self.LAST_INDEX)

        del self.heap[self.LAST_INDEX]
        self.size -= 1

        self.rebuild_heap(self.ROOT_INDEX)
        return val

    def rebuild_heap(self, i):
        if not self.is_leaf(i):
            larger_child_index = self.left_child(i)

            if self.right_child(i) < self.size:
                right_child_index = self.right_child(i)
                if self.heap[right_child_index] > self.heap[larger_child_index]:
                    larger_child_index = right_child_index

            if self.heap[i] < self.heap[larger_child_index]:
                self.swap(i, larger_child_index)
                self.rebuild_heap(larger_child_index)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def parent_index(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def is_leaf(self, i):
        return 2 * i + 2 > self.size

    def has_one_child(self, i):
        return 2 * i + 2 == self.size


def heap_sort(screen, matrix, nums):
    heap = Heap()

    for i in range(len(nums)):
        heap.add(nums[i])

        vals = np.concatenate([np.array(deepcopy(heap.heap)), nums[i+1:]])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        matrix_from_nums(vals, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()

    for i in range(len(nums)-1, 0, -1):
        nums[i] = heap.pop_root()

        vals = np.concatenate([np.array(deepcopy(heap.heap)), nums[i:]])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        matrix_from_nums(vals, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()
