from list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2, 3, '4')
    
    def test_add__should_add_element_and_return_list(self):
        self.int_list.add(4)
        expected = [1, 2, 3, 4]
        actual = self.int_list.get_data()
        self.assertEqual(actual, expected)
    
    def test_add__raise_ValueError_if_element_not_integer(self):
        with self.assertRaises(ValueError) as cm:
            self.int_list.add('5')
        self.assertEqual(str(cm.exception), "Element is not Integer")
    
    def test_remove_index__removes_element_on_given_index_and_returns_it(self):
        self.assertEqual(self.int_list.remove_index(1), 2)
        self.assertEqual(self.int_list.get_data(), [1, 3])
    
    def test_remove_index__should_raise_IndexError__if_given_index_incorrect(self):
        with self.assertRaises(IndexError) as cm:
            self.int_list.remove_index(3)
        self.assertEqual(str(cm.exception), "Index is out of range")
    
    def test_get__should_return_element_in_given_index(self):
        self.assertEqual(self.int_list.get(2), 3)
    
    def test_get__should_raise_IndexError__if_given_index_incorrect(self):
        with self.assertRaises(IndexError) as cm:
            self.int_list.get(3)
        self.assertEqual(str(cm.exception), "Index is out of range")


if __name__ == "__main__":
    unittest.main()
