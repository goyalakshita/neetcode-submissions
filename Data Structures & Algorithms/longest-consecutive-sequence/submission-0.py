class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=sorted(set(nums))
        count=1
        ans=1
        for i in range(len(s)-1):
            if s[i]+1==s[i+1]:
                count+=1
            else:
                count=1    
            ans=max(ans,count)    
        return ans        

        