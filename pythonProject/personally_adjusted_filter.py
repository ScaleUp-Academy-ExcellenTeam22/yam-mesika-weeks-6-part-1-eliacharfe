

def my_filter(func, iterable):
    """
    A generator function that implement the known function "filter" of python.
    :param func: A function.
    :param iterable: An iterable.
    :return: An iterator of the items in the iterable that return True from the function sent.
    """
    for item in iterable:
        if func(item):
            yield item


if __name__ == '__main__':
    for polyndrome in my_filter(lambda word: word == word[::-1],
                                ['abba', 'bob', 'week6_2', '1234', 'python', 'ArqqrA', 'WoW']):
        print(polyndrome)



