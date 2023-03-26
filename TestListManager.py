import unittest
from ListManager import ListManager

class TestListManager(unittest.TestCase):
    def setUp(self):
        self.list_manager = ListManager()

    def test_add_item(self):
        self.list_manager.add_item(1)
        self.assertEqual(self.list_manager.data, [1])
        self.list_manager.add_item(2)
        self.assertEqual(self.list_manager.data, [1, 2])

    def test_remove_item(self):
        self.list_manager.add_item(1)
        self.list_manager.add_item(2)
        self.list_manager.remove_item(1)
        self.assertEqual(self.list_manager.data, [2])
        self.list_manager.remove_item(3)
        self.assertEqual(self.list_manager.data, [2])

    def test_get_item(self):
        self.list_manager.add_item(1)
        self.list_manager.add_item(2)
        self.assertEqual(self.list_manager.get_item(0), 1)
        self.assertEqual(self.list_manager.get_item(1), 2)
        self.assertIsNone(self.list_manager.get_item(2))

    def test_count_items(self):
        self.assertEqual(self.list_manager.count_items(), 0)
        self.list_manager.add_item(1)
        self.assertEqual(self.list_manager.count_items(), 1)
        self.list_manager.add_item(2)
        self.assertEqual(self.list_manager.count_items(), 2)

    def test_reverse_items(self):
        self.list_manager.add_item(1)
        self.list_manager.add_item(2)
        self.list_manager.reverse_items()
        self.assertEqual(self.list_manager.data, [2, 1])

    def test_add_item_type_error(self):
        with self.assertRaises(TypeError):
            self.list_manager.add_item(None)

    def test_remove_item_type_error(self):
        with self.assertRaises(TypeError):
            self.list_manager.remove_item(None)

    def test_get_item_type_error(self):
        with self.assertRaises(TypeError):
            self.list_manager.get_item(None)

    def test_get_item_index_error(self):
        with self.assertRaises(IndexError):
            self.list_manager.get_item(-1)

if __name__ == "__main__":
    unittest.main()
