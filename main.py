import random

import eight_puzzle
from search import hill_climbing, simulated_annealing, simulated_annealing_full, exp_schedule
# problem = EightPuzzle((0, 1, 2, 3, 4, 5, 6, 7, 8))

# Models of the eight puzzle problem
# displaced tiles
PROBLEM_DISPLACED_TILES = eight_puzzle.EightPuzzleProblemDisplacedTiles()
# manhattan distance
PROBLEM_MANHATTAN_DISTANCE = eight_puzzle.EightPuzzleProblemManhattanDistance()
# The number of times to try solve the hill climbing problem
NUMBER_OF_TRIES = 30
# DISPLACED TILES HEURISTIC
# number of successes
NUMBER_DISPLACED_SUCCESS = 0
# average successes
AVG_DISPLACED_SUCCESS = 0
# MANHATTAN DISTANCE HEURISTIC
# number of successes
NUMBER_MANHATTAN_SUCCESS = 0
# average successes
AVG_MANHATTAN_SUCCESS = 0
NUMBER_MANHATTAN_SUCCESS_SA = 0

def calculate_results(problem, search, heuristic, iterations=NUMBER_OF_TRIES):
    # number of successes
    successes = 0
    # average successes
    avg_success = 0
    # avg heuristic result
    avg_heuristic = 0

    for i in range(iterations):
        result = search(problem)
        avg_heuristic += heuristic(result)
        if eight_puzzle.goal_test(result):
            successes += 1

    avg_success = successes / iterations
    avg_heuristic /= iterations
    print("Number of Tries: " + str(iterations))
    print("Number of Successes: " + str(successes))
    print("Average Successes: " + str(avg_success))
    print("Average Heuristic Value: " + str(avg_heuristic))


"""
for i in range(NUMBER_OF_TRIES):
    result = hill_climbing(PROBLEM_DISPLACED_TILES)
    if eight_puzzle.goal_test(result):
        NUMBER_DISPLACED_SUCCESS += 1

AVG_DISPLACED_SUCCESS = NUMBER_DISPLACED_SUCCESS / NUMBER_OF_TRIES
print("Number of Tries: " + str(NUMBER_OF_TRIES))
print("Number of Successes w/ Displaced Tiles Heuristic: " + str(NUMBER_DISPLACED_SUCCESS))
print("Average result using Displaced Tiles Heuristic: " + str(AVG_DISPLACED_SUCCESS))

for i in range(NUMBER_OF_TRIES):
    result = hill_climbing(PROBLEM_MANHATTAN_DISTANCE)
    if eight_puzzle.goal_test(result):
        NUMBER_MANHATTAN_SUCCESS += 1

AVG_MANHATTAN_SUCCESS = NUMBER_MANHATTAN_SUCCESS / NUMBER_OF_TRIES
print("Number of Tries: " + str(NUMBER_OF_TRIES))
print("Number of Successes w/ Manhattan Distance Heuristic: " + str(NUMBER_MANHATTAN_SUCCESS))
print("Average result using Manhattan Distance Heuristic: " + str(AVG_MANHATTAN_SUCCESS))

print("Demnonstrate that these algorithms can solve an Eight Puzzle")
print("Displaced Tiles")
print(hill_climbing(eight_puzzle.EightPuzzleProblemDisplacedTiles(True)))
print("Manhattan Distance")
print(hill_climbing(eight_puzzle.EightPuzzleProblemManhattanDistance(True)))

"""


calculate_results(PROBLEM_MANHATTAN_DISTANCE, simulated_annealing, eight_puzzle.manhattan_distance)



# for result in results:
#     itr += 1
#     print("iteration: " + str(itr) + " result: " + str(result))