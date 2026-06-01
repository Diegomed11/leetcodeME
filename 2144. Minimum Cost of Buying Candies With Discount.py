class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a=len(cost)
        if a<=2:
            return sum(cost)

        
        cost.sort(reverse=True)
        h=0
        for i in range(0,a,3):
            h+=cost[i]

            if i +1<a:
                h+=cost[i+1]
            
        return h
        