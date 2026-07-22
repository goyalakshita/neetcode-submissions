class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map2={}
        map1={}
        for ch in s:
            map2[ch]=map2.get(ch,0)+1
        for ch in t:
            map1[ch]=map1.get(ch,0)+1
        return map1==map2   
                   
        