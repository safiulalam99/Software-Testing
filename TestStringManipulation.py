import unittest
from StringManipulation import StringManipulation


class TestStringManipulation(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(StringManipulation.reverse_string("hello"), "olleh")
        self.assertEqual(StringManipulation.reverse_string("12345"), "54321")

    def test_is_palindrome(self):
        self.assertTrue(StringManipulation.is_palindrome("racecar"))
        self.assertFalse(StringManipulation.is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(StringManipulation.count_vowels("hello"), 2)
        self.assertEqual(StringManipulation.count_vowels("The quick brown fox jumps over the lazy dog"), 11)

    def test_count_substring(self):
        self.assertEqual(StringManipulation.count_substring("hello world, world", "world"), 2)
        self.assertEqual(StringManipulation.count_substring("hello world, world", "o"), 3)

    def test_replace_substring(self):
        self.assertEqual(StringManipulation.replace_substring("hello world, world", "world", "earth"), "hello earth, earth")
        self.assertEqual(StringManipulation.replace_substring("aaabbbccc", "a", "d"), "dddbbbccc")


if __name__ == '__main__':
    unittest.main()
