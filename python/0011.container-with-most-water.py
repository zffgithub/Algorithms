# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         0011.container-with-most-water
# Description:  
# Author:       zffgithub
# Email:       zffforgithub@gmail.com
# Date:         2020/10/2
# -------------------------------------------------------------------------------
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left, right = 0, length - 1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
