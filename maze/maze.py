MAZE_1 = """\
*...F\
"""

MAZE_2 = """\
#####
#*#F#
#.#.#
#...#
#####\
"""

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class MazeGame:
    def __init__(self):
        self.maze = MAZE_1
        self.pos = Position(1, 1)
    
    def print(self):
        print(self.maze)
    
    def left(self):
        pass

    def right(self):
        pass

# initialize game resources
game = MazeGame()
game.print()

# start the game loop

