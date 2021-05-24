class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c=0
        res=-1
        ln=len(haystack)
        flag=False
        if(haystack==needle or needle==""):
            return 0
        if(needle!=""):
            for i in range(ln):
                if(haystack[i]==needle[c]):
                    if(len(needle)>1):
                        c=1
                        for j in range(i+1,ln):
                            if(c<len(needle) and haystack[j]==needle[c]):
                                if(c==len(needle)-1):
                                    flag=True
                                    res=i
                                    break
                                else:
                                    c+=1
                            else:
                                c=0
                                break
                    else:
                        flag=True
                        res=i
                        break
                if(flag):
                    break
        return res
        
        
