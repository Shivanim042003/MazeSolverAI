import math

# Creating a 2D list with static values
matrix = [
    ['X', '0', '0', '0', 'x', 'x', 'x', 'x'],
    ['0', '0', '0', '0', '0', 'x', 'x', 'x'],
    ['x', 'x', '0', 'x', 'x', '0', '0', '0'],
    ['x', '0', '0', '0', '0', '0', '0', '0']
]

# matrix = [
#     ['X', '0', '0', '0'],
#     ['0', '0', '0', '0'],
#     ['x', 'x', '0', 'x'],
#     ['x', '0', '0', '0']
# ]

def print_maze(matrix, start_position, goal_position):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if (i, j) == start_position:
                print('S', end=' ')
            elif (i, j) == goal_position:
                print('G', end=' ')
            else:
                print(cell, end=' ')
        print()

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def neighbors(current_position):
    current_list = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_x = current_position[0] + dx
            new_y = current_position[1] + dy
            # Check if new coordinates are within the bounds of the grid
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                if (new_x, new_y) != current_position and matrix[new_x][new_y] != 'x':
                    current_list.append((new_x, new_y))
    return current_list




# def astar(start_position,goal_position):
#     current_position=start_position
#     path_list=[start_position]   
#     while(current_position!=goal_position):
#         neighbor_list = neighbors(current_position)
#         print("\nNeighbors of current position:", neighbor_list)
#         function_list=[]
#         for i in range(len(neighbor_list)):
#             function_list.append(manhattan_distance(neighbor_list[i], start_position) + euclidean_distance(neighbor_list[i], goal_position))
#         print(function_list)    
#         minimum_value = min(function_list)
#         print("Minimum value:", minimum_value)
#         for i in range(len(function_list)):
#             if(function_list[i]==minimum_value):
#                 current_position=neighbor_list[i]
#                 path_list.append(current_position)
#                 break;

#     print(path_list)

def astar(start_position, goal_position):
    path_list = [start_position]  # Initialize path_list with start_position
    current_position = start_position
    while current_position != goal_position:
        neighbor_list = neighbors(current_position)
        print("\nNeighbors of current position:", neighbor_list)
        function_list = []
        for neighbor in neighbor_list:
            function_list.append(euclidean_distance(neighbor, start_position) + manhattan_distance(neighbor, goal_position))
        print("Function values for neighbors:", function_list)
        minimum_value = min(function_list)
        print("Minimum value:", minimum_value)
        for i in range(len(function_list)):
            if function_list[i] == minimum_value:
                current_position = neighbor_list[i]
                path_list.append(current_position)
                break  # Once we update current_position, exit the loop
        if current_position == goal_position:  # Check if the goal has been reached
            break
    print("Path:", path_list)

print("Initial Maze:")
start_position = (0, 0)
goal_position = (3,7)


print_maze(matrix, start_position, goal_position)
astar(start_position,goal_position)