

def words_length(sentence):
    """
    Function that get a sentence of words and returns a list of the length of the words in it.
    :param sentence: The sentence.
    :return: A list of the length of the words in the sentence sent.
    """
    return [len(x) for x in sentence.split()]


if __name__ == '__main__':
    print("The list of the words length: "
          + str(words_length("Toto, I've a feeling we're not in Kansas anymore")))

