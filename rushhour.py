import vehicle

GOAL_VEHICLE = vehicle.Vehicle('X', 4, 2, 'H')

class RushHour(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles):
        """Create a new Rush Hour board.
        
        Arguments:
            vehicles: A list of Vehicle objects with distinct ids.

        Exceptions:
            ValueError: on multiple vehicles having same id
        """
        ids = [vehicle.id for vehicle in vehicles]
        uniq_ids = set(ids)
        if len(ids) != len(uniq_ids):
            raise ValueError('Multiple vehicles with same id.')

        self.vehicles = vehicles
        self.vehicle_map = {vehicle.id : vehicle for vehicle in vehicles}

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
        return GOAL_VEHICLE in self.vehicles
