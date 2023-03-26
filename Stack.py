class Stack:
    """
    Stack represents a simple stack data structure with limited functionality.
    """

    def __init__(self):
        """
        Initialize Stack with an empty stack.
        """
        self.stack = []

    def push(self, value):
        """
        Push a value onto the stack.

        :param value: The value to push onto the stack.
        :return: None
        """
        if value is None:
            raise TypeError("None is not allowed")
        self.stack.append(value)

    def pop(self):
        """
        Pop a value off the stack.

        :return: The popped value, or None if the stack is empty.
        """

        if not self.stack:
            return None
        return self.stack.pop()

    def size(self):
        """
        Get the size of the stack.

        :return: The size of the stack.
        """
        return len(self.stack)

    def is_empty(self):
        """
        Check if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def peek(self):
        """
        Get the top value of the stack without removing it.

        :return: The top value of the stack, or None if the stack is empty.
        """
        if not self.stack:
            return None
        return self.stack[-1]
