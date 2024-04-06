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

    def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
        delimiter_dict = {
                    "text": "text",
                    "**" : "bold",
                    "*" : "italic",
                    "`" : "code",}

        new_nodes = []
        for node in old_nodes:
            #Append all non TextNodes to the node list
            if not type(node) == TextNode:
                new_nodes.append(node)
                continue
            index = 0
            #While we have not encountered a delimiter, keep incrementing
            while not node._text[index] == delimiter:
                index += 1
                if index > len(node._text) - 1:
                    raise Exception("No delimiter found")
                
            #We can have a max of three Textnodes created
            #If index > 0, this means the first char in text was not delim, so we must create a textnode
            if index > 0:
                node1 = TextNode(node._text[:index], delimiter_dict.get("text"))
                new_nodes.append(node1)

            #Find the corresponding closing delim marker
            end_index = index + 1
            while not node._text[end_index] == delimiter:
                end_index += 1
                if end_index > len(node._text) - 1:
                    raise Exception("Closing delimiter does not exist")
                
            #Create second node, the textNode surrounded by 2 delims
            node2 = TextNode(node._text[index + 1:end_index], delimiter_dict.get(delimiter))
            new_nodes.append(node2)

            #Create third node if end_index != len(node.text) - 1, meaning there are more chars left in str
            if end_index < len(node._text) - 1:
                node3 = TextNode(node._text[end_index + 1:], delimiter_dict.get("text"))
                new_nodes.append(node3)
        return new_nodes
            

        #for each node
            #traverse through string one letter at a time until we encounter delimiter
            #upon encountering it, 