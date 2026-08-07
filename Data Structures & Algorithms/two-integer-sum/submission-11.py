class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        
        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                if hashmap[nums[i]] < i:
                    result = [hashmap[nums[i]], i]
                    return result
                else:
                    result = [i, hashmap[nums[i]]]
                    return result
            else:
                matchThis = target - nums[i]
                hashmap[matchThis] = i
                