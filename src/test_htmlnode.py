import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1","hello there", None, {"href": "https://www.google.com", "target": "blank"})
        node2 = HTMLNode("h1","hello there", None, {"href": "https://www.google.com", "target": "blank"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("h1","hello there", None, {"href": "https://www.google.com", "target": "blank"})
        node2 = HTMLNode("h2","hello there", None, {"href": "https://www.google.com", "target": "blank"})
        self.assertNotEqual(node, node2)
    
    def test_props_to_html(self):
        node = HTMLNode("h1","hello there", None, {"href": "https://www.google.com", "target": "blank"})
        self.assertEqual(node.props_to_html(),  "href=\"https://www.google.com\" target=\"blank\"")

    

if __name__ == "__main__":
    unittest.main()
