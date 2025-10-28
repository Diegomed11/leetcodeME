class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a=1

        while a**2<=num:
            if a**2==num:
                return True
            else:
                a+=1
        return False 