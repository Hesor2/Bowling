import unittest
from bowling import InvalidFrame, is_valid_frame, is_strike, is_spare, calc_points

class TestBowling(unittest.TestCase):
    def test_is_valid_frame(self):
        self.assertEqual(is_valid_frame([10,0]), True)
        self.assertEqual(is_valid_frame([0,10]), True)
        self.assertEqual(is_valid_frame([3,4]), True)
        self.assertEqual(is_valid_frame([0,0]), True)
        self.assertEqual(is_valid_frame([10]), False)
        self.assertEqual(is_valid_frame([0]), False)
        self.assertEqual(is_valid_frame([3,3,4]), False)
        self.assertEqual(is_valid_frame([10]), False)

    def test_is_strike(self):
        self.assertEqual(is_strike([10,0]), True)
        self.assertEqual(is_strike([0,10]), False)
        self.assertEqual(is_strike([9,0]), False)
        self.assertEqual(is_strike([4,4]), False)
        self.assertEqual(is_strike([9,1]), False)
        self.assertEqual(is_strike([1,9]), False)
        with self.assertRaises(InvalidFrame): is_strike([10,1])
        with self.assertRaises(InvalidFrame): is_strike([1,10])
        with self.assertRaises(InvalidFrame): is_strike([3,3,3])
    
    def test_is_spare(self):
        self.assertEqual(is_spare([10,0]), False)
        self.assertEqual(is_spare([0,10]), True)
        self.assertEqual(is_spare([9,1]), True)
        self.assertEqual(is_spare([1,9]), True)
        self.assertEqual(is_spare([4,4]), False)
        self.assertEqual(is_spare([9,0]), False)
        self.assertEqual(is_spare([0,9]), False)
        with self.assertRaises(InvalidFrame): is_spare([10,1])
        with self.assertRaises(InvalidFrame): is_spare([1,10])
        with self.assertRaises(InvalidFrame): is_spare([3,3,3])

    def test_calc_points(self):
        self.assertEqual(calc_points([[3,7],[10,0],[8,2],[8,1],[10,0],[3,4],[7,0],[5,5],[3,2],[2,5]]), [20,40,58,67,84,91,98,111,116,123])
        self.assertEqual(calc_points([[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,10]]), [30,60,90,120,150,180,210,240,270,300])
        self.assertEqual(calc_points([[3,7],[10,0],[8,2],[8,1],[10,0],[3,4],[7,0],[5,5],[3,2],[2,5]]), [20,40,58,67,84,91,98,111,116,123])

if __name__ == '__main__':
    unittest.main()