
class HTMLNode:
    """
tag - A string representing the HTML tag name 
value - A string representing the contents of the HTML tag 
children - A list of HTMLNode objects representing the children of this node
props - A dictionary of key-value pairs representing the attributes of the HTML tag. 
For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    """
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.__tag = tag
        self.__value = value
        self.__children = children
        self.__props = props

    def __eq__(self, other: object) -> bool:
        if self.__tag == other.__tag and\
        self.__value == other.__value and\
        self.__children == other.__children and\
        self.__props == other.__props:
            return True
        return False
    def __repr__(self) -> str:
        return f"HTMLNode({self.__tag}, {self.__value}, {self.__children}, {self.__props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = []
        for key, val in self.__props.items():
            combined = key + '="' + val +'"'
            html.append(combined)
            html.append(" ")
        #Remove the final extra space form the list
        return "".join(html)[:-1]