#!/usr/bin/env python3

import numpy as np

def transform(s1, s2):
    list1 = s1.split()
    list2 = s2.split()

    int_list1 = list(map(int, list1))
    int_list2 = list(map(int, list2))

    result = [a * b for a, b in zip(int_list1, int_list2)]

    return result

def main():
    pass
print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
