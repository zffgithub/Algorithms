# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         insert_sort
# Description:  
# Author:       zffgithub
# Email:       zffforgithub@gmail.com
# Date:         2020/10/2
# -------------------------------------------------------------------------------

def insert_sort(col):
    length = len(col)
    for index in range(1, length):
        while index > 0 and col[index - 1] > col[index]:
            col[index - 1], col[index] = col[index], col[index - 1]
            index -= 1
    return col


if __name__ == "__main__":
    col = [2, 0, 3, 1, 5, 7, 3, 97, 10]
    print(insert_sort(col))
