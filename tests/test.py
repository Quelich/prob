import unittest
import prob


class TestProbMethods(unittest.TestCase):

    def test_get_variance(self):
        A = [7.07, 7.00, 7.10, 6.97, 7.00, 7.03, 7.01, 7.01, 6.98, 7.08]
        mean = 7.025
        expect = 0.001938888888888887
        self.assertEqual(prob.get_variance(A, mean), expect)


if __name__ == '__main__':
    unittest.main()
