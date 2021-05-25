class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ln=len(nums)
        mid=ln//2
        res=0
        beg=0
        end=ln

        if(not nums or target<nums[0]):
            return res

        elif(nums[ln-1]<target):
            return ln

        else:
            while True:
                if(nums[mid]==target):
                    res=mid
                    break

                elif(end-beg==1 or beg>=end):
                    if(nums[beg]==target):
                        res=beg
                        break
                    elif(end==ln and nums[end-1]==target):
                        res=end-1
                        break
                    elif(end!=ln and nums[end]==target):
                        res=end
                        break
                    elif(nums[beg]>target):
                        res=beg
                        break

                    elif(end!=ln and nums[end]>target):
                        res=end
                        break
                    else:
                        res=end+1
                        break

                elif(nums[mid]<target):
                    beg=mid+1
                    mid=(beg+end)//2

                else:
                    end=mid-1
                    mid=(beg+end)//2

            return res
        
