import unittest
from StringFormatting import StringFormatting


class TestStringFormatting(unittest.TestCase):

    def test_to_uppercase(self):
        self.assertEqual(StringFormatting.to_uppercase("hello"), "HELLO")
        self.assertEqual(StringFormatting.to_uppercase("HelLo"), "HELLO")
        self.assertEqual(StringFormatting.to_uppercase(""), "")

    def test_to_lowercase(self):
        self.assertEqual(StringFormatting.to_lowercase("HELLO"), "hello")
        self.assertEqual(StringFormatting.to_lowercase("HelLo"), "hello")
        self.assertEqual(StringFormatting.to_lowercase(""), "")

    def test_capitalize_words(self):
        self.assertEqual(StringFormatting.capitalize_words("hello world"), "Hello World")
        self.assertEqual(StringFormatting.capitalize_words("HeLlO wOrLd"), "Hello World")
        self.assertEqual(StringFormatting.capitalize_words(""), "")

    def test_strip_whitespace(self):
        self.assertEqual(StringFormatting.strip_whitespace("  hello  "), "hello")
        self.assertEqual(StringFormatting.strip_whitespace("  HeLlO "), "HeLlO")
        self.assertEqual(StringFormatting.strip_whitespace(""), "")

    def test_replace_spaces_with_underscores(self):
        self.assertEqual(StringFormatting.replace_spaces_with_underscores("hello world"), "hello_world")
        self.assertEqual(StringFormatting.replace_spaces_with_underscores(" HeLlO  WoRlD "), "_HeLlO__WoRlD_")
        self.assertEqual(StringFormatting.replace_spaces_with_underscores(""), "")

    def test_to_uppercase_type_error(self):
        with self.assertRaises(TypeError):
            StringFormatting.to_uppercase(None)

    def test_to_lowercase_type_error(self):
        with self.assertRaises(TypeError):
            StringFormatting.to_lowercase(None)

    def test_capitalize_words_type_error(self):
        with self.assertRaises(TypeError):
            StringFormatting.capitalize_words(None)

    def test_strip_whitespace_type_error(self):
        with self.assertRaises(TypeError):
            StringFormatting.strip_whitespace(None)

    def test_replace_spaces_with_underscores_type_error(self):
        with self.assertRaises(TypeError):
            StringFormatting.replace_spaces_with_underscores(None)


if __name__ == '__main__':
    unittest.main()
