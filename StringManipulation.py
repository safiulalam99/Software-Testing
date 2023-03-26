class StringManipulation:
    """
    A class that provides simple string manipulation methods.
    """

    @staticmethod
    def reverse_string(s: str) -> str:
        """
        Reverse the input string.

        :param s: The input string
        :return: The reversed string
        """
        return s[::-1]

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Check if the input string is a palindrome.

        :param s: The input string
        :return: True if the string is a palindrome, False otherwise
        """
        return s == s[::-1]

    @staticmethod
    def count_vowels(s: str) -> int:
        """
        Count the number of vowels in the input string.

        :param s: The input string
        :return: The number of vowels in the string
        """
        return sum([1 for c in s.lower() if c in 'aeiou'])

    @staticmethod
    def count_substring(s: str, sub: str) -> int:
        """
        Count the occurrences of a substring in the input string.

        :param s: The input string
        :param sub: The substring to count
        :return: The number of occurrences of the substring in the string
        """
        return s.count(sub)

    @staticmethod
    def replace_substring(s: str, old_sub: str, new_sub: str) -> str:
        """
        Replace all occurrences of a substring with another substring.

        :param s: The input string
        :param old_sub: The substring to be replaced
        :param new_sub: The substring to replace with
        :return: The modified string with the replaced substrings
        """
        return s.replace(old_sub, new_sub)
