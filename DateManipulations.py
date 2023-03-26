import datetime

class DateManipulations:
    @staticmethod
    def days_between_dates(date1, date2):
        """
        Calculate the number of days between two dates.

        :param date1: The first date as a datetime.date object.
        :param date2: The second date as a datetime.date object.
        :return: The number of days between the two dates as an integer.
        """
        return abs((date2 - date1).days)

    @staticmethod
    def is_leap_year(year):
        """
        Check if a given year is a leap year.

        :param year: The year as an integer.
        :return: True if the year is a leap year, False otherwise.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def day_of_week(date):
        """
        Calculate the day of the week for a given date.

        :param date: The date as a datetime.date object.
        :return: The day of the week as an integer, where Monday is 0 and Sunday is 6.
        """
        return date.weekday()

    @staticmethod
    def add_days(date, days):
        """
        Add or subtract a number of days to a given date.

        :param date: The date as a datetime.date object.
        :param days: The number of days to add or subtract as an integer.
        :return: The resulting date as a datetime.date object.
        """
        return date + datetime.timedelta(days=days)

    @staticmethod
    def days_in_month(year, month):
        """
        Calculate the number of days in a month for a given year.

        :param year: The year as an integer.
        :param month: The month as an integer.
        :return: The number of days in the given month and year as an integer.
        """
        if month == 2:
            return 29 if DateManipulations.is_leap_year(year) else 28
        elif month in {4, 6, 9, 11}:
            return 30
        else:
            return 31
