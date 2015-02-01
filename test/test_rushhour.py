import unittest
import rushhour
import vehicle

class TestRushHour(unittest.TestCase):

    def test_create_from_set(self):
        v = vehicle.Vehicle('X', 0, 0, 'H')
        r = rushhour.RushHour(set([v]))
        self.assertEqual(r.vehicles, set([v]))
        self.assertEqual(r.vehicle_map, {v.id: v})

    def test_create_from_dict(self):
        v = vehicle.Vehicle('X', 0, 0, 'H')
        r = rushhour.RushHour({v.id: v})
        self.assertEqual(r.vehicles, set([v]))
        self.assertEqual(r.vehicle_map, {v.id: v})

    def test_create_from_invalid(self):
        v = vehicle.Vehicle('X', 0, 0, 'H')
        with self.assertRaises(TypeError):
            r = rushhour.RushHour(v)

        with self.assertRaises(TypeError):
            r = rushhour.RushHour([v])

        with self.assertRaises(TypeError):
            r = rushhour.RushHour(tuple([v]))

    def test_duplicate_vehicle_id(self):
        v1 = vehicle.Vehicle('X', 0, 0, 'H')
        v2 = vehicle.Vehicle('X', 1, 1, 'V')
        with self.assertRaises(ValueError):
            r = rushhour.RushHour(set([v1,v2]))

    def test_get_board_horizontal_top_left(self):
        v = vehicle.Vehicle('X', 0, 0, 'H')
        r = rushhour.RushHour(set([v]))
        expected_board = [['X', 'X', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_vertical_top_left(self):
        v = vehicle.Vehicle('X', 0, 0, 'V')
        r = rushhour.RushHour(set([v]))
        expected_board = [['X', ' ', ' ', ' ', ' ', ' '],
                          ['X', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_horizontal_top_right(self):
        v = vehicle.Vehicle('X', 4, 0, 'H')
        r = rushhour.RushHour(set([v]))
        expected_board = [[' ', ' ', ' ', ' ', 'X', 'X'],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_vertical_top_right(self):
        v = vehicle.Vehicle('X', 5, 0, 'V')
        r = rushhour.RushHour(set([v]))
        expected_board = [[' ', ' ', ' ', ' ', ' ', 'X'],
                          [' ', ' ', ' ', ' ', ' ', 'X'],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_horizontal_bottom_left(self):
        v = vehicle.Vehicle('X', 0, 5, 'H')
        r = rushhour.RushHour(set([v]))
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          ['X', 'X', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_vertical_bottom_left(self):
        v = vehicle.Vehicle('X', 0, 4, 'V')
        r = rushhour.RushHour(set([v]))
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          ['X', ' ', ' ', ' ', ' ', ' '],
                          ['X', ' ', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_horizontal_bottom_right(self):
        v = vehicle.Vehicle('X', 4, 5, 'H')
        r = rushhour.RushHour(set([v]))
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', 'X', 'X']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_vertical_bottom_right(self):
        v = vehicle.Vehicle('X', 5, 4, 'V')
        r = rushhour.RushHour(set([v]))
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', 'X'],
                          [' ', ' ', ' ', ' ', ' ', 'X']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_alternative_car(self):
        v = vehicle.Vehicle('A', 0, 0, 'H')
        r = rushhour.RushHour(set([v]))
        expected_board = [['A', 'A', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_get_board_alternative_truck(self):
        v = vehicle.Vehicle('O', 0, 0, 'H')
        r = rushhour.RushHour(set([v]))
        expected_board = [['O', 'O', 'O', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']]
        for line, expected_line in zip(r.get_board(), expected_board):
            self.assertEqual(line, expected_line)

    def test_solved(self):
        v = vehicle.Vehicle('X', 4, 2, 'H')
        r = rushhour.RushHour(set([v]))
        self.assertTrue(r.solved())

    def test_not_solved(self):
        v = vehicle.Vehicle('X', 0, 0, 'H')
        r = rushhour.RushHour(set([v]))
        self.assertFalse(r.solved())

    def test_moves_one_car_left_edge_horizontal(self):
        v = vehicle.Vehicle('X', 0, 0, 'H')
        expected_v = vehicle.Vehicle('X', 1, 0, 'H')
        r = rushhour.RushHour(set([v]))
        expected_r = rushhour.RushHour(set([expected_v]))
        next_moves = set([move for move in r.moves()])
        self.assertEqual(1, len(next_moves))
        self.assertIn(expected_r, next_moves)

    def test_moves_one_car_middle_horizontal(self):
        v = vehicle.Vehicle('X', 1, 0, 'H')
        expected_v1 = vehicle.Vehicle('X', 0, 0, 'H')
        expected_v2 = vehicle.Vehicle('X', 2, 0, 'H')
        r = rushhour.RushHour(set([v]))
        expected_r1 = rushhour.RushHour(set([expected_v1]))
        expected_r2 = rushhour.RushHour(set([expected_v2]))
        next_moves = set([move for move in r.moves()])
        self.assertEqual(2, len(next_moves))
        self.assertIn(expected_r1, next_moves)
        self.assertIn(expected_r2, next_moves)

    def test_moves_one_car_right_edge_horizontal(self):
        v = vehicle.Vehicle('X', 4, 0, 'H')
        expected_v = vehicle.Vehicle('X', 3, 0, 'H')
        r = rushhour.RushHour(set([v]))
        expected_r = rushhour.RushHour(set([expected_v]))
        next_moves = set([move for move in r.moves()])
        self.assertEqual(1, len(next_moves))
        self.assertIn(expected_r, next_moves)

    def test_moves_one_car_top_edge_vertical(self):
        v = vehicle.Vehicle('X', 0, 0, 'V')
        expected_v = vehicle.Vehicle('X', 0, 1, 'V')
        r = rushhour.RushHour(set([v]))
        expected_r = rushhour.RushHour(set([expected_v]))
        next_moves = set([move for move in r.moves()])
        self.assertEqual(1, len(next_moves))
        self.assertIn(expected_r, next_moves)

    def test_moves_one_car_middle_vertical(self):
        v = vehicle.Vehicle('X', 0, 1, 'V')
        expected_v1 = vehicle.Vehicle('X', 0, 0, 'V')
        expected_v2 = vehicle.Vehicle('X', 0, 2, 'V')
        r = rushhour.RushHour(set([v]))
        expected_r1 = rushhour.RushHour(set([expected_v1]))
        expected_r2 = rushhour.RushHour(set([expected_v2]))
        next_moves = set([move for move in r.moves()])
        self.assertEqual(2, len(next_moves))
        self.assertIn(expected_r1, next_moves)
        self.assertIn(expected_r2, next_moves)

    def test_moves_one_car_bottom_edge_vertical(self):
        v = vehicle.Vehicle('X', 0, 4, 'V')
        expected_v = vehicle.Vehicle('X', 0, 3, 'V')
        r = rushhour.RushHour(set([v]))
        expected_r = rushhour.RushHour(set([expected_v]))
        next_moves = set([move for move in r.moves()])
        self.assertEqual(1, len(next_moves))
        self.assertIn(expected_r, next_moves)
