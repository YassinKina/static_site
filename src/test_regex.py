import unittest
import markdown


class TestRegex(unittest.TestCase):
    def test_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expresion = markdown.extract_markdown_images(text)
        self.assertEqual(expresion,[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])          

    def test_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expression = markdown.extract_markdown_links(text)
        self.assertEqual(expression, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expression = markdown.extract_markdown_links(text)
        self.assertEqual(expression, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
    
    def test_diff_text_formats(self):
        text = "Click [here](https://www.example.com) for more information"
        expression = markdown.extract_markdown_links(text)
        self.assertEqual(expression, [("here", "https://www.example.com")])

        text = "This is a [link](https://www.example.com/page?id=123&category=foo)"
        expression = markdown.extract_markdown_links(text)
        self.assertEqual(expression, [("link", "https://www.example.com/page?id=123&category=foo")])
    
    def test_no_description(self):
        text = "You can find more info [here](https://www.example.com/info)"
        expression = markdown.extract_markdown_links(text)
        self.assertEqual(expression, [("here", "https://www.example.com/info")])

        text = "Learn more [here](https://www.example.com/my%20page)"
        expression = markdown.extract_markdown_links(text)
        self.assertEqual(expression, [("here", "https://www.example.com/my%20page")])
                
    

                         


    


if __name__ == "__main__":
    unittest.main()
