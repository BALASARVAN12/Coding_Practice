#Question:
'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.You must implement a solution with a linear runtime complexity and use only constant extra space.'''
#Examples:
'''
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

#Code:
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor
    
#Example-1:
nums = [2, 2, 1]
solution = Solution()
result = solution.singleNumber(nums)
print(result)

#Time complexity: O(n)
#Space complexity: O(1)