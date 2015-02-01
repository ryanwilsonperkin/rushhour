import unittest
import vehicle

class TestVehicle(unittest.TestCase):

    def test_create(self):
        v = vehicle.Vehicle('X', 0, 1, 'H')
        self.assertEqual(v.id, 'X')
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 1)
        self.assertEqual(v.orientation, 'H')

    def test_create_cars(self):
        for id in vehicle.CAR_IDS:
            v = vehicle.Vehicle(id, 0, 0, 'H')
            self.assertEqual(v.id, id)
            self.assertEqual(v.length, 2)

    def test_create_trucks(self):
        for id in vehicle.TRUCK_IDS:
            v = vehicle.Vehicle(id, 0, 0, 'H')
            self.assertEqual(v.id, id)
            self.assertEqual(v.length, 3)

    def test_create_bad_id(self):
        with self.assertRaises(ValueError):
            vehicle.Vehicle(None, 0, 0, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('Z', 0, 0, 'H')

    def test_create_bad_x(self):
        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', None, 0, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', -1, 0, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 6, 0, 'H')

    def test_create_bad_y(self):
        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, None, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, -1, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, 6, 'H')

    def test_create_bad_orientation(self):
        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, 0, None)

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, 0, 'h')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, 0, 'v')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, 0, 'x')

    def test_create_bad_config(self):
        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 5, 5, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 5, 5, 'V')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 5, 0, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('X', 0, 5, 'V')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('O', 4, 0, 'H')

        with self.assertRaises(ValueError):
            vehicle.Vehicle('O', 0, 4, 'V')

    def test_equality(self):
        v1 = vehicle.Vehicle('X', 0, 0, 'H')
        v2 = vehicle.Vehicle('X', 0, 0, 'H')
        self.assertEqual(v1, v2)

    def test_inequality(self):
        v1 = vehicle.Vehicle('X', 0, 0, 'H')
        v2 = vehicle.Vehicle('A', 0, 0, 'H')
        v3 = vehicle.Vehicle('X', 1, 0, 'H')
        v4 = vehicle.Vehicle('X', 0, 1, 'H')
        v5 = vehicle.Vehicle('X', 0, 0, 'V')
        self.assertNotEqual(v1, v2)
        self.assertNotEqual(v1, v4)
        self.assertNotEqual(v1, v4)
        self.assertNotEqual(v1, v5)
