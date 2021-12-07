TITLE = "Algorithm Visualizer"
FINAL_DELAY = 2  # seconds
FPS = 60

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
assert SCREEN_WIDTH == SCREEN_WIDTH

NODE_WIDTH = 5
NODE_HEIGHT = 5
assert SCREEN_WIDTH % NODE_WIDTH == 0
assert SCREEN_HEIGHT % NODE_HEIGHT == 0

NUM_COLS = SCREEN_WIDTH // NODE_WIDTH
NUM_ROWS = SCREEN_HEIGHT // NODE_HEIGHT

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
