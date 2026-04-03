class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                if i < hashmap[nums[i]]:
                    return [i,hashmap[nums[i]]]
                else:
                    return [hashmap[nums[i]], i]
            else:
                result = target - nums[i]
                hashmap.update({result : i})
