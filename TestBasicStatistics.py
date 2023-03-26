import unittest
from BasicStatistics import BasicStatistics


class TestBasicStatistics(unittest.TestCase):

    def setUp(self):
        self.statistics = BasicStatistics()
        self.sample_data = [3, 5, 7, 9, 11]

    # Tests for mean method
    def test_mean_positive(self):
        self.assertEqual(self.statistics.mean(self.sample_data), 7)

    def test_mean_negative(self):
        self.assertEqual(self.statistics.mean([-3, -5, -7, -9, -11]), -7)

    def test_mean_mixed(self):
        self.assertEqual(self.statistics.mean([-3, 5, 7, -9, 11]), 2.2)

    # Tests for median method
    def test_median_odd(self):
        self.assertEqual(self.statistics.median(self.sample_data), 7)

    def test_median_even(self):
        self.assertEqual(self.statistics.median([3, 5, 7, 9]), 6)

    def test_median_mixed(self):
        self.assertEqual(self.statistics.median([-3, 5, 7, -9, 11]), 5)

    # Tests for mode method
    def test_mode_unique(self):
        self.assertEqual(self.statistics.mode(
            self.sample_data), self.sample_data)

    def test_mode_multiple(self):
        self.assertEqual(self.statistics.mode([3, 5, 7, 9, 7, 5]), [5, 7])

    def test_mode_single(self):
        self.assertEqual(self.statistics.mode([3, 5, 7, 9, 7]), [7])

    # Tests for range_of_numbers method
    def test_range_positive(self):
        self.assertEqual(self.statistics.range_of_numbers(self.sample_data), 8)

    def test_range_negative(self):
        self.assertEqual(self.statistics.range_of_numbers(
            [-3, -5, -7, -9, -11]), 8)

    def test_range_mixed(self):
        self.assertEqual(self.statistics.range_of_numbers(
            [-3, 5, 7, -9, 11]), 20)

    # Tests for standard_deviation method


def test_standard_deviation_positive(self):
    self.assertAlmostEqual(self.statistics.standard_deviation(
        self.sample_data), 3.1623, places=4)


def test_standard_deviation_negative(self):
    self.assertAlmostEqual(self.statistics.standard_deviation(
        [-3, -5, -7, -9, -11]), 3.1623, places=4)


def test_standard_deviation_mixed(self):
    self.assertAlmostEqual(self.statistics.standard_deviation(
        [-3, 5, 7, -9, 11]), 8.0747, places=4)

    # Exception handling tests
    def test_empty_list_exception(self):
        with self.assertRaises(Exception) as context:
            self.statistics.mean([])
        self.assertEqual(str(context.exception), "List cannot be empty")


if __name__ == "__main__":
    unittest.main()
