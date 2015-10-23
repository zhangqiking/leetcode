class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        i=0
        while i<length-1:
            if nums[i+1]==nums[i]:
                del nums[i+1]
                length=len(nums)
            else:
                i=i+1
        length=len(nums)
        return length
