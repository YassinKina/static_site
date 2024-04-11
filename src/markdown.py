import re
from textnode import TextNode
"""
Takes in raw text as input an returns a list of tuples
"""
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_delimiter( old_nodes, delimiter, text_type):
        new_nodes = []
        for old_node in old_nodes:
            #Append all nodes that are not TextNodes
            if type(old_node) != TextNode:
                new_nodes.append(old_node)
                continue
            
            split_nodes = []
            sections = old_node._text.split(delimiter)
            if len(sections) % 2 == 0:
                raise ValueError("Invalid markdown")
            
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextNode.text_type_text))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))
            new_nodes.extend(split_nodes)
        return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node._text_type != TextNode.text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node._text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextNode.text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextNode.text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node._text_type != TextNode.text_type_text:
            new_nodes.append(old_node)
            continue

        original_text = old_node._text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
            new_nodes.append(TextNode(link[0], TextNode.text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextNode.text_type_text))
    return new_nodes

