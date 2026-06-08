class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        menores=[]
        mayores=[]
        iguales=[]


        for i in nums:
            if i > pivot:
                mayores.append(i)
            elif i < pivot:
                menores.append(i)
            else:
                iguales.append(i)

        menores.extend(iguales)
        menores.extend(mayores)
        
        return menores

      