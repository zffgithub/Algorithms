# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         bubble_sort
# Description:  
# Author:       zffgithub
# Email:       zffforgithub@gmail.com
# Date:         2020/10/2
# -------------------------------------------------------------------------------

def bubble_sort(col):
    length = len(col)
    for loop in range(length - 1):
        s = True
        for index in range(length - 1 - loop):
            if col[index] > col[index + 1]:
                s = False
                col[index], col[index + 1] = col[index + 1], col[index]
        print(col)
        if s:
            break
    return col


if __name__ == "__main__":
    col = [2, 0, 3, 1, 5, 7, 3, 97, 10]
    print(bubble_sort(col))
