class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """


        s=set()

        powx=1

        while powx <= bound:
            powy=1
            while powx+powy <= bound:
                s.add(powx+powy)

                powy*=y
                if powy == 1:
                    break

            powx*=x
            if powx == 1:
                break    
            
        return list(s)