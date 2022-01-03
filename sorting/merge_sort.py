from sorting.sorting_helpers import *
import pygame
import sys


def merge_sort(screen, matrix, nums, start, end):
    if start < end:
        mid = (start + end) // 2

        merge_sort(screen, matrix, nums, start, mid)
        merge_sort(screen, matrix, nums, mid+1, end)

        merge(screen, matrix, nums, start, mid, end)


def merge(screen, matrix, nums, start, mid, end):
    tmp = [None] * (end - start + 1)

    i, j = start, mid + 1
    k = 0

    # Merge lists in ascending order
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    # Add remaining values to list
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1

    while j <= end:
        tmp[k] = nums[j]
        j += 1
        k += 1

    # Copy values back to list
    for x in range(len(tmp)):
        nums[start+x] = tmp[x]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update Pygame screen
        matrix_from_nums(nums, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()
