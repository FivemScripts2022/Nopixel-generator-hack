import numpy as np
import random


game_array = np.zeros((7,7))


def generate_solution(game_array):
    current_index = [0, 0]
    starting_index = [0, 0]
    available_direction = ["down", "right"]
    solution_array = game_array
    top_left_value = random.randint(1,3)
    solution_array[0, 0] = top_left_value
    original_direction = random.choice(available_direction)
    solution_steps = []
    if original_direction == "right":
        current_index = [0, top_left_value]
        starting_index = [0, top_left_value]
    else:
        current_index = [top_left_value, 0]
        starting_index = [top_left_value, 0]
    solution_steps.append(top_left_value)
    solution_steps.append(original_direction)

    print(current_index)
    while current_index != [6, 6]:
        if current_index[0] != 6 and current_index[1] != 6:
            direction = random.choice(available_direction)
            if direction == "right":
                available_moves = 7 - current_index[1] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0], current_index[1] + movement]
            elif direction == "down":
                available_moves = 7 - current_index[0] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0] + movement, current_index[1]]
        else:
            if current_index[0] == 6 and current_index[1] != 6:
                direction = "right"
                available_moves = 7 - current_index[1] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0], current_index[1] + movement]
            elif current_index[0] != 6 and current_index[1] == 6:
                direction = "down"
                available_moves = 7 - current_index[0] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0] + movement, current_index[1]]
            else:
                continue
        solution_steps.append(movement)
        solution_steps.append(direction)
        solution_array[starting_index[0], starting_index[1]] = movement
        starting_index = current_index
    for x in range(7):
        for y in range(7):
            if solution_array[x,y] == 0:
                solution_array[x, y] = random.randint(1,4)
    return(solution_array)


game_array = generate_solution(game_array)
print(game_array)


