class Queue:
    """
    Queue represents a simple queue data structure with limited functionality.
    """

    def __init__(self):
        """
        Initialize Queue with an empty queue.
        """
        self.queue = []

    def enqueue(self, value):
        """
        Enqueue a value onto the queue.
        
        :param value: The value to enqueue onto the queue.
        :return: None
        """
        if value is None:
            raise TypeError("Value cannot be None.")
        self.queue.append(value)
        
    def dequeue(self):
        """
        Dequeue a value from the queue.
        
        :return: The dequeued value, or None if the queue is empty.
        """
        if not self.queue:
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.queue.pop(0)

    def size(self):
        """
        Get the size of the queue.
        
        :return: The size of the queue.
        """
        if not self.queue:
            raise IndexError("Cannot get the size of an empty queue.")
        return len(self.queue)

    def is_empty(self):
        """
        Check if the queue is empty.
        
        :return: True if the queue is empty, False otherwise.
        :raise: IndexError if checking the empty state of the queue is not allowed.
        """
        if len(self.queue) == 0:
            raise IndexError("Cannot check if an empty queue is empty.")
        return False
    
    def peek(self):
        """
        Get the front value of the queue without removing it.
        
        :return: The front value of the queue, or None if the queue is empty.
        """
        if not self.queue:
            raise IndexError("Cannot peek at an empty queue.")
        return self.queue[0]
