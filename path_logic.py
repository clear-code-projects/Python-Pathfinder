# from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

matrix = [
  [1, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1]]

# 1. create the grid with the nodes 
grid = Grid(matrix=matrix)

# get start and end point 
start = grid.node(0, 0)
end = grid.node(5, 2)

# create a finder with the movement style 
finder = AStarFinder() # can add DiagonalMovement as argument here with never or always + more

# returns a list with the path and the amount of times the finder had to run to get the path 
path, runs = finder.find_path(start, end, grid)


# print result 
print(path)