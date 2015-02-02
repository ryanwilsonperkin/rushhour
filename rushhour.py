from collections import deque
from vehicle import Vehicle

GOAL_VEHICLE = Vehicle('X', 4, 2, 'H')

class RushHour(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles):
        """Create a new Rush Hour board.
        
        Arguments:
            vehicles: a set of Vehicle objects.
        """
        self.vehicles = vehicles

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.vehicles == other.vehicles

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        s = '-' * 8 + '\n'
        for line in self.get_board():
            s += '|{0}|\n'.format(''.join(line))
        s += '-' * 8 + '\n'
        return s

    def get_board(self):
        """Representation of the Rush Hour board as a 2D list of strings"""
        board = [[' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ']]
        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    board[y][x+i] = vehicle.id
            else:
                for i in range(vehicle.length):
                    board[y+i][x] = vehicle.id
        return board

    def solved(self):
        """Returns true if the board is in a solved state."""
        return GOAL_VEHICLE in self.vehicles

    def moves(self):
        """Return iterator of next possible moves."""
        board = self.get_board()
        for v in self.vehicles:
            if v.orientation == 'H':
                if v.x - 1 >= 0 and board[v.y][v.x - 1] == ' ':
                    new_v = Vehicle(v.id, v.x - 1, v.y, v.orientation)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield RushHour(new_vehicles)
                if v.x + v.length <= 5 and board[v.y][v.x + v.length] == ' ':
                    new_v = Vehicle(v.id, v.x + 1, v.y, v.orientation)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield RushHour(new_vehicles)
            else:
                if v.y - 1 >= 0 and board[v.y - 1][v.x] == ' ':
                    new_v = Vehicle(v.id, v.x, v.y - 1, v.orientation)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield RushHour(new_vehicles)
                if v.y + v.length <= 5 and board[v.y + v.length][v.x] == ' ':
                    new_v = Vehicle(v.id, v.x, v.y + 1, v.orientation)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield RushHour(new_vehicles)

def load_file(rushhour_file):
    vehicles = []
    for line in rushhour_file:
        line = line[:-1] if line.endswith('\n') else line
        id, x, y, orientation = line
        vehicles.append(Vehicle(id, int(x), int(y), orientation))
    return RushHour(set(vehicles))

def get_solutions_breadth_first(r, max_depth=25):
    """
    Yields solutions to given RushHour board using breadth first search.
    Yields nothing if no solutions are encountered within max_depth moves.

    Arguments:
        r: A RushHour board.

    Keyword Arguments:
        max_depth: Maximum depth to traverse in search (default=25)
    """
    visited = set()
    solutions = set()
    depth_states = dict()

    queue = deque()
    queue.appendleft((r, tuple()))
    while len(queue) != 0:
        board, path = queue.pop()
        new_path = path + tuple([board])

        depth_states[len(new_path)] = depth_states.get(len(new_path), 0) + 1

        if len(new_path) >= max_depth:
            break

        if board in visited:
            continue
        else:
            visited.add(board)

        if board.solved():
            solutions.add(new_path)

        for move in board.moves():
            queue.appendleft((move, new_path))

    return {'visited': visited,
            'solutions': solutions,
            'depth_states': depth_states}
