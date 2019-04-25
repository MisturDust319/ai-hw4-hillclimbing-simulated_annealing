import numpy as np
import eight_puzzle

ITERATIONS = 10000
ACTIONS = ["up", "right", "down", "left"]
START_BOARD = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# displaced tiles
DISPLACED_TILES_RESULTS = []
for i in range(ITERATIONS):
    new_board = eight_puzzle.mess_up(START_BOARD, ACTIONS, 10)
    result = eight_puzzle.n_out_of_order(new_board)
    DISPLACED_TILES_RESULTS.append(result)

DISPLACED_TILES_RANGE = np.ptp(DISPLACED_TILES_RESULTS)
print("Range of values for Displaced Tiles: " + str(DISPLACED_TILES_RANGE))

# manhattan distance
MANHATTAN_DISTANCE_RESULTS = []
for i in range(ITERATIONS):
    new_board = eight_puzzle.mess_up(START_BOARD, ACTIONS, 10)
    result = eight_puzzle.manhattan_distance(new_board)
    MANHATTAN_DISTANCE_RESULTS.append(result)

MANHATTAN_DISTANCE_RANGE = np.ptp(MANHATTAN_DISTANCE_RESULTS)
print("Range of values for Manhattan Distance: " + str(MANHATTAN_DISTANCE_RANGE))