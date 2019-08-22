import unittest
from listutil import unique


class ListUtilTest(unittest.TestCase):

    def test_single_item_list(self):
        self.assertListEqual(['hi'], unique(['hi']))
        self.assertListEqual(['hello'], unique(['hello']))
        self.assertListEqual(['world'], unique(['world']))
        self.assertListEqual(['a'], unique(['a']))

    def test_empty_list(self):
        self.assertListEqual([], unique([]))
        self.assertListEqual([], unique([    ]))

    def test_single_item_list_many_times(self):
        self.assertListEqual(['a'], unique(["a", "a", "a", "a", "a"]))
        self.assertListEqual(['hi'], unique(['hi', 'hi', 'hi', 'hi']))
        self.assertListEqual(['hello'], unique(['hello', 'hello', 'hello']))
        self.assertListEqual(['world'], unique(['world', 'world']))

    def test_many_item_list_many_times(self):
        self.assertListEqual(['a', 'b', 'c', 'd', 'e'], unique(["a", "a", "a", "a", "b", "b", "c", "c", "d", "d", "e"]))
        self.assertListEqual(['1', '2', '3', '4', '5'], unique(["1", "1", "2", "2", "3", "3", "4", "4", "5", "5"]))
        self.assertListEqual([1,  2,  4,], unique([1, 2, 2, 4 , 4]))
        self.assertListEqual([6, 8, 9, 10, 11], unique([6, 6, 6, 8, 8, 9, 10, 10, 10, 10, 11]))
        self.assertListEqual(['2.0', '-2.0', '@', '%'], unique(["2.0", "-2.0", "@", "%", "%"]))

    def test_many_item_list_many_times_many_list(self):
        self.assertListEqual([1, 2, 4, [1, 2, 3], [1, 3, 4]],unique([1, 2, 2, 4, [1, 2, 3], [1, 3, 4], [1, 3, 4], 1]))
        self.assertListEqual(["a", "b", 4, ["c", "d", "e"]], unique(["a", "a", "a", "b", 4, ["c", "d", "e"],
                                                                     ["c", "d", "e"], ["c", "d", "e"]]))
        self.assertListEqual(["1", "2", 3, 4, 5, ["1", "2", "3"], [1, 2, 3]], unique(["1", "2", "2", "2", 3, 3, 4, 4, 4,
                                                                                      5, ["1", "2", "3"], [1, 2, 3],
                                                                                      [1, 2, 3]]))
        self.assertListEqual([11111, 2222, 333, [4, 5, 6], [0], 0], unique([11111, 11111, 11111, 2222, 2222, 333,
                                                                            [4, 5, 6], [0], 0, 0]))

    def test_many_items_no_duplicate(self):
        self.assertListEqual(['1', '2', '-3', '3'], unique(["1", "2", "-3", "3"]))
        self.assertListEqual(['hi', 'hello', 'sawaddee'], unique(["hi", "hello", "sawaddee"]))
        self.assertListEqual([4, 5, 6], unique([4, 5, 6]))

    def test_argument_not_a_list(self):
        with self.assertRaises(TypeError):
            unique(9.9)

        with self.assertRaises(TypeError):
            unique(888888)

        with self.assertRaises(TypeError):
            unique("5")

if __name__ == '__main__':
    unittest.main()

