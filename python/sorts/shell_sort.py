# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         shell_sort
# Description:  
# Author:       zffgithub
# Email:       zffforgithub@gmail.com
# Date:         2020/10/2
# -------------------------------------------------------------------------------

def shell_sort(col):
    length = len(col)
    gap = int(length / 2)
    while gap > 0:
        for index in range(gap, length):
            ci = index
            cur = col[index]
            while ci - gap >= 0 and cur < col[ci - gap]:
                col[ci] = col[ci - gap]
                ci -= gap
            col[ci] = cur
        gap = int(gap / 2)
    return col


if __name__ == "__main__":
    col = [2, 0, 3, 1, 5, 7, 3, 97, 10]
    print(shell_sort(col))
