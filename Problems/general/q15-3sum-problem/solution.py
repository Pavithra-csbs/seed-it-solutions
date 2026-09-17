"""
Problem: Q15 - 3Sum Problem
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-17
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

import sys, json
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right = i+1,n-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total ==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left]==nums[left+1]:
                        left +=1
                    while left < right and nums[right]==nums[right-1]:
                        right -=1
                    
                    left +=1
                    right -=1
                elif total <0:
                    left +=1
                else:
                    right -=1
        return res

if __name__ == '__main__':
    import sys, json
    args = json.loads(sys.stdin.readline())
    nums = args[0] if (args and isinstance(args[0], list)) else args
    print(json.dumps(Solution().threeSum(nums)))
