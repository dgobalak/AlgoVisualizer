from helpers import *
import pygame 

def bubble_sort(screen, matrix, clock):
    nums = randomize_sorting_matrix(matrix)
    screen.fill(BLACK)
    clock.tick(FPS)

    for i in range(len(nums)):
        screen.fill(BLACK)
        clock.tick(FPS)

        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(nums) - 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return

                if nums[i+1] <= nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    sorted = False

                matrix_from_nums(nums, matrix)
                draw_matrix(screen, matrix)
                pygame.display.flip()