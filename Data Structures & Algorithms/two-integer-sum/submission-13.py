class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i in range(len(nums)):

            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]

            difference = target - nums[i]
        #    if difference in hashmap:
         #       return [hashmap[difference], i]
            if difference not in hashmap:
                hashmap[difference] = i
             