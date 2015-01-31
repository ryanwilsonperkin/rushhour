import unittest
import vehicleconfig

class TestVehicleConfig(unittest.TestCase):

    def test_create(self):
        v = vehicleconfig.VehicleConfig('X', 0, 1, 'H')
        self.assertEqual(v.id, 'X')
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 1)
        self.assertEqual(v.orientation, 'H')

    def test_create_cars(self):
        for id in vehicleconfig.CAR_IDS:
            v = vehicleconfig.VehicleConfig(id, 0, 0, 'H')
            self.assertEqual(v.id, id)
            self.assertEqual(v.length, 2)

    def test_create_trucks(self):
        for id in vehicleconfig.TRUCK_IDS:
            v = vehicleconfig.VehicleConfig(id, 0, 0, 'H')
            self.assertEqual(v.id, id)
            self.assertEqual(v.length, 3)

    def test_create_bad_id(self):
        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig(None, 0, 0, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('Z', 0, 0, 'H')

    def test_create_bad_x(self):
        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', None, 0, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', -1, 0, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 6, 0, 'H')

    def test_create_bad_y(self):
        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, None, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, -1, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, 6, 'H')

    def test_create_bad_orientation(self):
        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, 0, None)

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, 0, 'h')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, 0, 'v')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, 0, 'x')

    def test_create_bad_config(self):
        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 5, 5, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 5, 5, 'V')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 5, 0, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('X', 0, 5, 'V')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('O', 4, 0, 'H')

        with self.assertRaises(ValueError):
            vehicleconfig.VehicleConfig('O', 0, 4, 'V')
