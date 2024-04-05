from leafnode import LeafNode

class TextNode:

    def __init__(self, text, text_type, url=None) -> None:
        self._text = text
        self._text_type = text_type
        self._url= url

    def __eq__(self, other: object) -> bool:
        return (
            self._text == other._text and
            self._text_type == other._text_type and
            self._url == other._url
        )
       
    
    def __repr__(self) -> str:
        return f"TextNode({self._text}, {self._text_type}, {self._url})"
    
    def text_node_to_html_node(text_node):
        #Ensure we only work with valid text_types
        if text_node._text_type not in "text,bold,italic,code,link,image":
            raise Exception("Invalid text type")
        leaf_node = None
        #Create the correct type of leaf node depending on the text type
        match text_node._text_type:
            case "text":
                leaf_node = LeafNode(text_node._text)
            case "bold":
                leaf_node = LeafNode(text_node._text, "b")
            case "italic":
                leaf_node = LeafNode(text_node._text, "i")
            case "code":
                leaf_node = LeafNode(text_node._text, "code")
            case "link":
                leaf_node = LeafNode(text_node._text, "a", props="href")
            case "image":
                leaf_node = LeafNode(text_node._text, "img", {"src": "alt"})
        return leaf_node

