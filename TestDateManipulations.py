import unittest
import datetime
from DateManipulations import DateManipulations

class TestDateManipulations(unittest.TestCase):

    def setUp(self):
        self.date_manipulations = DateManipulations()

    # Tests for days_between_dates method
    def test_days_between_dates(self):
        date1 = datetime.date(2020, 1, 1)
        date2 = datetime.date(2020, 1, 31)
        self.assertEqual(self.date_manipulations.days_between_dates(date1, date2), 30)

    def test_days_between_dates_same(self):
        date = datetime.date(2020, 1, 1)
        self.assertEqual(self.date_manipulations.days_between_dates(date, date), 0)

    def test_days_between_dates_reversed(self):
        date1 = datetime.date(2020, 1, 1)
        date2 = datetime.date(2020, 1, 31)
        self.assertEqual(self.date_manipulations.days_between_dates(date2, date1), 30)

    # Tests for is_leap_year method
    def test_is_leap_year_true(self):
        self.assertTrue(self.date_manipulations.is_leap_year(2000))

    def test_is_leap_year_false(self):
        self.assertFalse(self.date_manipulations.is_leap_year(1900))

    def test_is_leap_year_non_century(self):
        self.assertTrue(self.date_manipulations.is_leap_year(2020))

    # Tests for day_of_week method
    def test_day_of_week(self):
        date = datetime.date(2020, 1, 1)
        self.assertEqual(self.date_manipulations.day_of_week(date), 2)

    def test_day_of_week_sunday(self):
        date = datetime.date(2020, 1, 5)
        self.assertEqual(self.date_manipulations.day_of_week(date), 6)

    def test_day_of_week_monday(self):
        date = datetime.date(2020, 1, 6)
        self.assertEqual(self.date_manipulations.day_of_week(date), 0)

    # Tests for add_days method
    def test_add_days_positive(self):
        date = datetime.date(2020, 1, 1)
        result = datetime.date(2020, 1, 11)
        self.assertEqual(self.date_manipulations.add_days(date, 10), result)

    def test_add_days_negative(self):
        date = datetime.date(2020, 1, 11)
        result = datetime.date(2020, 1, 1)
        self.assertEqual(self.date_manipulations.add_days(date, -10), result)

    def test_add_days_zero(self):
        date = datetime.date(2020, 1, 1)
        self.assertEqual(self.date_manipulations.add_days(date, 0), date)

    # Tests for days_in_month method
    def test_days_in_month_31(self):
        self.assertEqual(self.date_manipulations.days_in_month(2020, 1), 31)

    def test_days_in_month_30(self):
        self.assertEqual(self.date_manipulations.days_in_month(2020, 4), 30)

    def test_days_in_month_29(self):
        self.assertEqual(self.date_manipulations.days_in_month(2020, 2), 29)

    def test_days_in_month_28(self):
        self.assertEqual(self.date_manipulations.days_in_month(2021, 2), 28)

if __name__ == "__main__":
    unittest.main()
