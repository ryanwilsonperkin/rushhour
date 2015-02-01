CAR_IDS = {'X', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'}
TRUCK_IDS = {'O', 'P', 'Q', 'R'}

class Vehicle(object):
    """A configuration of a single vehicle."""

    def __init__(self, id, x, y, orientation):
        """Create a new vehicle.
        
        Arguments:
            id: a valid car or truck id character
            x: the x coordinate of the top left corner of the vehicle (0-5)
            y: the y coordinate of the top left corner of the vehicle (0-5)
            orientation: either the vehicle is vertical (V) or horizontal (H)

        Exceptions:
            ValueError: on invalid id, x, y, or orientation
        """
        if id in CAR_IDS:
            self.id = id
            self.length = 2
        elif id in TRUCK_IDS:
            self.id = id
            self.length = 3
        else:
            raise ValueError('Invalid id {0}'.format(id))

        if 0 <= x <= 5:
            self.x = x
        else:
            raise ValueError('Invalid x {0}'.format(x))

        if 0 <= y <= 5:
            self.y = y
        else:
            raise ValueError('Invalid y {0}'.format(y))

        if orientation == 'H':
            self.orientation = orientation
            x_end = self.x + (self.length - 1)
            y_end = self.y
        elif orientation == 'V':
            self.orientation = orientation
            x_end = self.x
            y_end = self.y + (self.length - 1)
        else:
            raise ValueError('Invalid orientation {0}'.format(orientation))

        if x_end > 5 or y_end > 5:
            raise ValueError('Invalid configuration')

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
