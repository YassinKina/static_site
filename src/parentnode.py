from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if not self._tag:
            raise ValueError("No tag provided")
        if not self._children:
            raise ValueError("No children provided")
        
        html = f"<{self._tag}>"
        # <p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>
        #Loop through children and concat results
        print("My children are:", self._children, "\n")
        for leaf in self._children:
            html += leaf.to_html() 
        html += f"</{self._tag}>"
        return html
        
