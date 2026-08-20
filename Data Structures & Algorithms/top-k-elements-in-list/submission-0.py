class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        freq : list[int] = []

        checkThis : list[int] = []

        returnThis : list[int] = []

        for i in range(len(nums)):
            # Populate hashmap with counts
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else: 
                hashmap[nums[i]] += 1
        
        for key in hashmap: 
            freq.append(hashmap[key])
        
        freq.sort(reverse=True)

        for i in range(k):
            checkThis.append(freq[i])
        
        for key in hashmap: 
            if hashmap[key] in checkThis:
                returnThis.append(key)
        
        return returnThis

            



            



# if the value of the current key is greater than the previous key, drop the previous key out of the set dependent on the drop limit, the drop limit is defined as # keys  - k 

# This involves me storing the value of the previous key, in a hashset and comparing it against that. 
# This is to prevent a nested for loop (o(n ^2), there is a problem in that what about the first element?
# Would a later element be troublesome? if it has a lower count? 



        