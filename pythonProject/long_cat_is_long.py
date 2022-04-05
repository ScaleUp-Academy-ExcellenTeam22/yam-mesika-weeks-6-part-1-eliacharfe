

def count_words(some_text):
    """
    The function gets a text, first cuts all characters that are not letters or whitespaces, then returns
    a dictionary of the words (as keys) and their length (as value)
    :param some_text: The text sent
    :return: A dictionary of the words (as keys) and their length (as value)
    """
    my_clean_text = ''.join(char for char in some_text if char.isalnum() or char.isspace())
    return {word: len(word) for word in my_clean_text.split()}


if __name__ == '__main__':
    text = """
     You see, wire telegraph is a kind of a very, very long cat.
     You pull his tail in New York and his head is meowing in Los Angeles.
     Do you understand this?
     And radio operates exactly the same way: you send signals here, they receive them there.
     The only difference is that there is no cat.
     """
    print(count_words(text))

