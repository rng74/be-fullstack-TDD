def get_max(a, b):
    return a if a > b else b


def get_max_without_arguments():
    raise "No arguments"


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    maxx = -float('inf')
    for i in args:
        maxx = i if (i > maxx) else maxx
    return maxx


def get_max_with_one_or_more_arguments(first, *args):
    return first if first > get_max_with_many_arguments(*args) else get_max_with_many_arguments(*args)


def get_max_bounded(*args, low, high):
    maxx = -float('inf')
    for i in args:
        if i >= low and i <= high:
            maxx = i if i > maxx else maxx;
    return maxx


def make_max(*, low, high):
    def inner(first, *args):
        return get_max_bounded(first, *args, low = low, high = high)
    return inner
