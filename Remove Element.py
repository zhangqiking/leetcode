class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        length=len(nums)
        while i<length: 
            if nums[i]==val:
                del nums[i]
                length=len(nums)
            else:
                i=i+1
        return length
        
        
