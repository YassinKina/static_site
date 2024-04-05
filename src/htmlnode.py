
class HTMLNode:
    """
tag - A string representing the HTML tag name 
value - A string representing the contents of the HTML tag 
children - A list of HTMLNode objects representing the children of this node
props - A dictionary of key-value pairs representing the attributes of the HTML tag. 
For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    """
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self._tag = tag
        self._value = value
        self._children = children
        self._props = props

    def __eq__(self, other: object) -> bool:
            return (
                self._tag == other._tag and
                self._value == other._value and
                self._children == other._children and
                self._props == other._props
            )

    def __repr__(self) -> str:
        return f"HTMLNode({self._tag}, {self._value}, {self._children}, {self._props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = []
        for key, val in self._props.items():
            combined = key + '="' + val +'"'
            html.append(combined)
            html.append(" ")
        #Remove the final extra space form the list
        return "".join(html)[:-1]