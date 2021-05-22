class Solution:
    def isValid(self, s: str) -> bool:
    
        matched=[0 for i in range(len(s))]
        open_brace=0
        find=''
        for i in range (len(s)):
            
            if(s[i]==')' or s[i]=='}' or s[i]==']'):
                
                if(s[i]==')'):
                    find='('
                elif(s[i]=='}'):
                    find='{'
                elif(s[i]==']'):
                    find='['
                    
                
                if(i==0):
                    return False
                
                else:
                    j=i-1
                    
                    while j>=0:
                        
                        if(matched[j]==0 and s[j]==find):
                                matched[i]=1
                                matched[j]=1
                                open_brace-=1
                                find=''
                                break
                                
                        elif(matched[j]==0):
                            return False
                                
                        j-=1
                        
            else:
                open_brace+=1
     
        if(open_brace==0 and find==''):
            return True
        else:
            return False
