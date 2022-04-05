import time


def calculate_time_takes_function_to_run(function, *args):
    """
    A function that check out the time that to the function passed to run on the arguments passed.
    :param function: A function.
    :param args: A list of arguments.
    :return: The time that the function passed run on the arguments passed.
    """
    start_time = time.time()
    function(args)
    return time.time() - start_time


if __name__ == '__main__':
    print(calculate_time_takes_function_to_run(print, "Hello"))
    print(calculate_time_takes_function_to_run(zip, [1, 2, 3], [4, 5, 6]))



