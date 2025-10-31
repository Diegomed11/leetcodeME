class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        c={}

        for i in nums:
            
            c[i]=c.get(i,0)+1
            if c[i]==2:
                res.append(i)
        return res