import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]   ,)
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_recursive(self):
        node = ParentNode("p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]   ,)
        ]   ,)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")
        
    def test_single_parent_with_leaves(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

    def test_nested_parents_with_leaves(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "Italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p></p>")
        
    def test_nested_parents_with_leaves2(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "Italic text"),
                        LeafNode(None, "Normal text"),
                        ParentNode("p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "Italic text"),
                                LeafNode(None, "Normal text"),
                            ]
                        ),
                    ]
                ),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p></p></p>")



    

if __name__ == "__main__":
    unittest.main()
