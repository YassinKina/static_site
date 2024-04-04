class TextNode:

    def __init__(self, text, text_type, url=None) -> None:
        self.__text = text
        self.__text_type = text_type
        self.__url= url

    def __eq__(self, other: object) -> bool:
        if self.__text == other.__text and\
            self.__text_type == other.__text_type and\
            self.__url == other.__url:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.__text}, {self.__text_type}, {self.__url})"

