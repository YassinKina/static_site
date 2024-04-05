from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(value, tag, props=props)

    def __eq__(self, other: object) -> bool:
        return super().__eq__(other)

    def to_html(self):
        if not self._value:
            raise ValueError
        #Return raw text if there is no tag
        if not self._tag:
            return self._value
        
        #Insert tag in correct spot and return result string
        result = ""
        if self._props:
            result = f'<{self._tag} {self.props_to_html()}>{self._value}</{self._tag}>'
        else:
            result = f'<{self._tag}>{self._value}</{self._tag}>'
        return result
            