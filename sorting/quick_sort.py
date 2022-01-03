from sorting.sorting_helpers import *
import pygame
import sys


def quick_sort(screen, matrix, nums, a, b):
    if a < b:
        pivot_index = partition(screen, matrix, nums, a, b)
        quick_sort(screen, matrix, nums, a, pivot_index-1)
        quick_sort(screen, matrix, nums, pivot_index+1, b)


def partition(screen, matrix, nums, a, b):
    # We'll use the last index as the pivot
    pivot_val = nums[b]
    left, right = a, b-1

    partitioned = False
    while not partitioned:
        while nums[left] < pivot_val:
            left += 1
        while nums[right] > pivot_val:
            right -= 1

        if left < right:
            swap(screen, matrix, nums, left, right)
            left += 1
            right -= 1
        else:
            partitioned = True

    swap(screen, matrix, nums, b, left)
    return left


def swap(screen, matrix, nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    matrix_from_nums(nums, matrix)
    draw_matrix(screen, matrix)
    pygame.display.flip()
