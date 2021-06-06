class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        mySum = 0
        result = sys.maxsize
        for end in range(len(nums)):
            mySum = mySum + nums[end]
            #if the sum crosses target then keep moving start
            while mySum >= target:
                result = min(result, (end - start + 1))
                mySum = mySum - nums[start]
                start += 1
        return result if result != sys.maxsize else 0
                
        