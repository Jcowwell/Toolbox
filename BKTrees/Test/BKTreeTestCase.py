import unittest
from ..BKTree import TreeNode, BKTree

class BKTreeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.words: set = {"books", "cake", "boo", "boon", "cook", "cake", "cape", "cart"} 
        self.tree: BKTree = BKTree(root = 'book')

        for word in self.words:
            self.tree.insert(word)

    def test_BKTree_lookup(self):

        self.assertEqual(
            self.tree.lookup(
                w='cool'
            ),
            'cook'
        )

if __name__ == '__main__':
    unittest.main()
