class ListManager:
    """
    ListManager represents a simple list manager that can perform various list operations.
    """

    def __init__(self):
        """
        Initialize ListManager with an empty list.
        """
        self.data = []

    def add_item(self, item):
        """
        Add an item to the list.
        
        :param item: The item to add to the list.
        :return: The updated list.
        """
        if item is None:
            raise TypeError("Item cannot be None.")
        self.data.append(item)
        return self.data

    def remove_item(self, item):
        """
        Remove an item from the list if it exists.
        
        :param item: The item to remove from the list.
        :return: The updated list.
        """
        if item is None:
            raise TypeError("Item cannot be None.")
        if item in self.data:
            self.data.remove(item)
        return self.data

    def get_item(self, index):
        """
        Get the item at the specified index in the list.
        
        :param index: The index of the item to retrieve.
        :return: The item at the specified index, or None if the index is out of bounds.
        """
        if index is None:
            raise TypeError("Index cannot be None.")
        if index < 0:
            raise IndexError("Index cannot be negative.")
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def count_items(self):
        """
        Count the number of items in the list.
        
        :return: The number of items in the list.
        """
        return len(self.data)

    def reverse_items(self):
        """
        Reverse the order of the items in the list.
        
        :return: The updated list with the order reversed.
        """
        self.data.reverse()
        return self.data
