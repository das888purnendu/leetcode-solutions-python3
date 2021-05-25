class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ln = len(nums)
        if(ln>1000):  # it is DP alo for faster process
            mx,res = nums[0],nums[0]
            for i in range(ln):
                if(mx+nums[i]>nums[i]):
                    mx+=nums[i]
                else:
                    mx=nums[i]
                if(mx>res):
                    res=mx
            return res
        
        elif(ln>1): # it is n**2 algo
            sm=nums[0]
            for i in range(len(nums)):
                for j in range(i,len(nums)):
                    tmp=sum(nums[i:j+1])
                    if(tmp>sm):
                        sm=tmp
            return sm
        else:
            return nums[0]
