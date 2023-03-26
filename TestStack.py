import unittest
from Stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty(self):
        self.assertIsNone(self.stack.pop())

    def test_size(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_false(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)

    def test_peek_empty(self):
        self.assertIsNone(self.stack.peek())

    def test_push_type_error(self):
        with self.assertRaises(TypeError):
            self.stack.push(None)

if __name__ == '__main__':
    unittest.main()
