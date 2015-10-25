class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        length=len(nums)
        while i<length:
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
            i+=1
        return length
