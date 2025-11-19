class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        if original not in nums:
            return original
        
        a=original
        while a in nums:
            a=a*2
        return a