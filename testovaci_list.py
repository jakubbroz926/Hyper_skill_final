import time
list_a = [[(1, 3), (2, 3), (2, 4)], [(1, 3), (2, 4), (4, 4)]]


def print_list(lst):
    for i in lst:
        if isinstance(i, tuple):
            print(i)
        else:
            print_list(i)


print_list(list_a)
print(time.perf_counter())