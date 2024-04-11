

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
            
 

                         


    


if __name__ == "__main__":
    unittest.main()
