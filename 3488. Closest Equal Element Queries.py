import bisect

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        total_nums = len(nums)
        posiciones = {}

        for i, num in enumerate(nums):
            if num not in posiciones:
                posiciones[num] = []
            posiciones[num].append(i)

        res = []

        for q in queries:
            if q < 0 or q >= total_nums:
                res.append(-1)
                continue 

            n = nums[q]
            indices = posiciones[n]

            if len(indices) < 2:
                res.append(-1)
                continue 
            
            minds = float('inf')
            idx_pos = bisect.bisect_left(indices, q)
            

            candidatos = {idx_pos - 1, idx_pos, idx_pos + 1, 0, len(indices) - 1}
            
            for k in candidatos:
                if 0 <= k < len(indices):
                    s = indices[k]
                    if s != q:
                        lin = abs(s - q)
                        cir = total_nums - lin
                        actual = min(lin, cir)
                        if actual < minds:
                            minds = actual
            res.append(minds)
        return res