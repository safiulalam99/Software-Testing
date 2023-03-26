class StringFormatting:
    @staticmethod
    def to_uppercase(s: str) -> str:
        """Convert a string to uppercase."""
        if s is None:
            raise TypeError("Input string cannot be None")
        return s.upper()

    @staticmethod
    def to_lowercase(s: str) -> str:
        """Convert a string to lowercase."""
        if s is None:
            raise TypeError("Input string cannot be None")
        return s.lower()

    @staticmethod
    def capitalize_words(s: str) -> str:
        """Capitalize the first letter of each word in a string."""
        if s is None:
            raise TypeError("Input string cannot be None")
        return s.title()

    @staticmethod
    def strip_whitespace(s: str) -> str:
        """Remove leading and trailing whitespace from a string."""
        if s is None:
            raise TypeError("Input string cannot be None")
        return s.strip()

    @staticmethod
    def replace_spaces_with_underscores(s: str) -> str:
        """Replace spaces with underscores in a string."""
        if s is None:
            raise TypeError("Input string cannot be None")
        return s.replace(" ", "_")
