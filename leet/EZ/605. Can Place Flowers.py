class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            toplant = True
            if flowerbed[i] == 0:
                if  i!=0 and len(flowerbed) >= 2:
                    toplant = flowerbed[i-1] == 0
                if toplant and i!= len(flowerbed)-1 and len(flowerbed) >= 2:
                    toplant = flowerbed[i+1] == 0
            else:
                toplant = False
            if toplant:
                flowerbed[i] = 1
                n -= 1

        return n==0


print(Solution.canPlaceFlowers(Solution,[0,0,1,0,0],1))