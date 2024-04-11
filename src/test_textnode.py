import unittest

from textnode import TextNode
from parentnode import ParentNode
from leafnode import LeafNode
import markdown as markdown


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "italics", "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://www.amazon.com")
        node2 = TextNode("This is a text node", "italics", "https://www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = markdown.split_nodes_delimiter([node,], "`", "code")
        self.assertEqual(new_nodes, 
                         [
                            TextNode("This is text with a ", "text"),
                            TextNode("code block", "code"),
                            TextNode(" word", "text"),
                         ])
    def test_delimiter2(self):
        # Additional tests
        node2 = TextNode("Another `code` block", "text")
        new_nodes2 = markdown.split_nodes_delimiter([node2,], "`", "code")
        self.assertEqual(new_nodes2, 
                         [
                            TextNode("Another ", "text"),
                            TextNode("code", "code"),
                            TextNode(" block", "text"),
                         ])
        
    def test_delimiter_first_char_delim(self):
        node3 = TextNode("`First word Second` words", "text")
        new_nodes3 = markdown.split_nodes_delimiter([node3,], "`", "code")
        self.assertEqual(new_nodes3, 
                         [
                            TextNode("First word Second", "code"),
                            TextNode(" words", "text"),
                         ])
    def test_delimiter_last_char_delim(self):
        node3 = TextNode("First `word Second words`", "text")
        new_nodes3 = markdown.split_nodes_delimiter([node3,], "`", "code")
        self.assertEqual(new_nodes3, 
                         [
                            TextNode("First ", "text"),
                            TextNode("word Second words", "code")
                         ])
    def test_delimiter_parent(self):
        node3 = TextNode("First `word Second words`", "text")
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        new_nodes3 = markdown.split_nodes_delimiter([node3, node], "`", "code")
        self.assertEqual(new_nodes3, 
                         [
                            TextNode("First ", "text"),
                            TextNode("word Second words", "code"),
                            ParentNode("p",
                                    [
                                    LeafNode("b", "Bold text"),
                                    LeafNode(None, "Normal text"),
                                    LeafNode("i", "Italic text"),
                                    LeafNode(None, "Normal text")
                                    ])
                            ] )
        
                         


    


if __name__ == "__main__":
    unittest.main()
