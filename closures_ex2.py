import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):  # the star here means we can add in any number of arguments into the function
        logging.info('Running "{}" with arguments {}').format(func.__name__, args)
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


add_logger = logger(add)
