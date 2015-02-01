import vehicle

GOAL_VEHICLE = vehicle.Vehicle('X', 4, 2, 'H')

class RushHour(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles):
        """Create a new Rush Hour board.
        
        Arguments:
            vehicles: either a set of Vehicle objects or a dictionary of
                      mappings from id to Vehicle objects.

        Exceptions:
            TypeError: on improper type of vehicles param
            ValueError: on multiple vehicles having same id
        """
        if type(vehicles) == set:
            self.vehicles = vehicles
            self.vehicle_map = {vehicle.id : vehicle for vehicle in vehicles}
        elif type(vehicles) == dict:
            self.vehicle_map = vehicles
            self.vehicles = set(vehicles.values())
        else:
            raise TypeError('vehicles must be either list or dict')

        if len(self.vehicles) != len(self.vehicle_map.keys()):
            raise ValueError('Multiple vehicles with same id.')

    def __eq__(self, other):
        return self.vehicles == other.vehicles

    def __repr__(self):
        s = '-' * 8 + '\n'
        for line in self.get_board():
            s += '|{0}|\n'.format(''.join(line))
        s += '-' * 8 + '\n'
        return s

    def get_board(self):
        """Representation of the Rush Hour board as a 2D list of strings"""
        board = [[' ' for i in range(6)] for j in range(6)]
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
