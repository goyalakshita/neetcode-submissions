class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr=[]
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                diff=prices[j]-prices[i]
                if diff<=0:
                    arr.append(0)
                else:
                    arr.append(diff)    
        if arr:
            return max(arr)
        else:
            return 0    
        