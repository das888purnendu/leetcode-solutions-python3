class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val)>=1:
            nums.remove(val)
        return len(nums)
        
