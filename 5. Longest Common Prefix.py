class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        s=strs[0]
        flag=True
        res=""
        
        for i in range(len(s)):
            for j in range(1,len(strs)):
                
                if(i>len(strs[j])-1):
                    flag=False
                    break
    
                elif(len(strs[j])>i and s[i]!=strs[j][i]):
                    flag=False
                    break
                    
            if(flag==False):
                break
            else:
                res+=s[i]
                
        return res
