class Solution(object):
    def __init__(self):
        self.out=0
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.find(nums,0,0,target)
        return self.out
    
    def find(self,nums,c,sm,target):

        if c == len(nums):
            if sm== target:
                self.out+=1

        else:
            self.find(nums,c+1,sm-nums[c],target)

            self.find(nums,c+1,sm+nums[c],target)
        