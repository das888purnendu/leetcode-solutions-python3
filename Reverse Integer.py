class Solution:
    def reverse(self, x):
        
        fl=False
        if(x<0):
            fl=True
            x=abs(x)
            
        x=str(x)
        
        if(fl):
            res= int("-"+x[::-1])
        else:
            res= int(x[::-1])
        
        if res > (2**31) or res < (-2**31):
            return 0
        else:
            return res
            
        
