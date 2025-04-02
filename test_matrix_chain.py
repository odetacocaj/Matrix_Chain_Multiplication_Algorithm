import unittest
from matrix_chain import compute_matrix_chain
from utils import format_optimal_order

class TestMatrixChain(unittest.TestCase):
    def test_case_1(self):
        dimensions = [30, 35, 35, 20, 20]
        costs, splits = compute_matrix_chain(dimensions)
        self.assertEqual(costs[1][len(dimensions) - 1], 57500) 

    def test_case_2(self):
        dimensions = [10,20,25,19,15,12,13,24,27,28,90,76,34,45,87,99,22,7,22,11,23]
        costs, splits = compute_matrix_chain(dimensions)
        self.assertEqual(costs[1][len(dimensions) - 1],  226838)
        self.assertEqual(format_optimal_order(splits, 1, len(dimensions) - 1), "(((A1 x (A2 x (A3 x (A4 x (A5 x (A6 x (A7 x (A8 x (A9 x (A10 x (A11 x (A12 x (A13 x (A14 x (A15 x (A16 x A17)))))))))))))))) x (A18 x A19)) x A20)")

    def test_case_3(self):
        dimensions = [20, 30, 40, 25, 33, 20]
        costs, splits = compute_matrix_chain(dimensions)
        self.assertEqual(format_optimal_order(splits, 1, len(dimensions) - 1), "(((A1 x A2) x A3) x (A4 x A5))")  


if __name__ == '__main__':
    unittest.main()
