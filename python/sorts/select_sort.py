# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         select_sort
# Description:  
# Author:       zffgithub
# Email:       zffforgithub@gmail.com
# Date:         2020/10/2
# -------------------------------------------------------------------------------

def select_sort(col):
    length = len(col)
    for loop in range(length - 1):
        least = loop
        for index in range(loop + 1, length):
            if col[least] > col[index]:
                least = index
        if least != loop:
            col[loop], col[least] = col[least], col[loop]
    return col


if __name__ == "__main__":
    col = [2, 0, 3, 1, 5, 7, 3, 97, 10]
    print(select_sort(col))
