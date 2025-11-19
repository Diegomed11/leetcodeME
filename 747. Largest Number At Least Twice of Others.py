class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        idx= nums.index(m)

        for i in nums:
            if i == m:
                continue
            
            if m<2*i:
                return -1
        
        return idx
