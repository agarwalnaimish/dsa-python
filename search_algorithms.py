"""

Common Search Algorithms

@author: Naimish Agarwal

"""


def binary_search(key, sorted_list):
    a = sorted_list
    low = 0
    high = len(a) - 1

    while (low <= high):
        mid = low + (high - low) / 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            high = mid - 1
        elif a[mid] < key:
            low = mid + 1

    return None
