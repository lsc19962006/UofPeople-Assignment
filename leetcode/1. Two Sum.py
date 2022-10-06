class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            p=target-nums[i]
            num=nums
            num[i]=999999999
            if p in num:
                return [i,num.index(p)]