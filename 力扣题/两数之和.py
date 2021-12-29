from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = [] #hashtable
        
        for i , num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
        hashtable[num[i]] = i 
        return []