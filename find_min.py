def get_min(a, b):
    return a if a < b else b

def get_min_without_arguments():
    raise "No arguments"

def get_min_with_one_argument(x):
    return x

def get_min_with_many_arguments(*args):
    mini = float('inf')
    for i in args:
        mini = i if (i < mini) else mini
    return mini

def get_min_with_one_or_more_arguments(first, *args):
    return first if first < get_min_with_many_arguments(*args) else get_min_with_many_arguments(*args)

def get_min_bounded(*args, low, high):
    mini = float('inf')
    for i in args:
        if i >= low and i <= high:
            mini = i if i < mini else mini;
    return mini

def make_min(*, low, high):
    def inner(first, *args):
        return get_min_bounded(first, *args, low = low, high = high)
    return inner
