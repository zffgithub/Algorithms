# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         0001.two-sum
# Description:  
# Author:       zffgithub
# Email:       zffforgithub@gmail.com
# Date:         2020/10/2
# -------------------------------------------------------------------------------
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        check_num = {}
        for i in range(length):
            check_num.setdefault(target - nums[i], i + 1)
            if check_num.get(nums[i]) and check_num[nums[i]] != i + 1:
                return [check_num[nums[i]] - 1, i]
