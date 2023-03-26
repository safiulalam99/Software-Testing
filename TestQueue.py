# test_Queue.py
import unittest
from Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

    def test_size(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)


    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1)

    def test_enqueue_type_error(self):
        with self.assertRaises(TypeError):
            self.queue.enqueue(None)

    def test_dequeue_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_size_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.size()

    def test_is_empty_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.is_empty()

    def test_peek_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.peek()

if __name__ == "__main__":
    unittest.main()
