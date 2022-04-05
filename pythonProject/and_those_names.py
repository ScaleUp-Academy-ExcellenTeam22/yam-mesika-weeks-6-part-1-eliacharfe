

def upper_first_letter_of_name(name: str) -> str:
    """
    Get a name and return the name with the first letter as uppercase instead of lowercase.
    :param name: A string containing a name.
    :return: the name with the first letter as uppercase instead of lowercase.
    """
    return name[0].upper() + name[1:]


def full_names(firsts_names: list[str], lasts_names: list[str], min_length: int = 0) -> list:
    """
    Gets a list of first names and a list of last names and an optional parameter min_length and return
    a list of all combinations of first names with last names that are greater or equal to the min_length
    if passed (by default min_length is 0), that after will turn each first/last name to uppercase at
    the first letter.
    :param firsts_names: A list of first names.
    :param lasts_names: A list of last names.
    :param min_length: (optional) The full names that are greater than this parameter.
    :return: List of all full names.
    """
    return [upper_first_letter_of_name(first) + " " + upper_first_letter_of_name(last)
            for first in firsts_names for last in lasts_names
            if len(first) + len(last) + 1 >= min_length]


if __name__ == '__main__':
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']

    print(full_names(first_names, last_names))
    print(full_names(first_names, last_names, 10))

