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
