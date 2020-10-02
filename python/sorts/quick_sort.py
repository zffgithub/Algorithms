# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         quick_sort
# Description:  
# Author:       zffgithub
# Email:       zffforgithub@gmail.com
# Date:         2020/10/2
# -------------------------------------------------------------------------------

def quick_sort(col):
    length = len(col)
    if length < 2:
        return col
    pivot = col.pop()
    left = []
    right = []
    for item in col:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    col = [2, 0, 3, 1, 5, 7, 3, 97, 10]
    print(quick_sort(col))
