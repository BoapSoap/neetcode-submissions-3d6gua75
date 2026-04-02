class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      checkDict = {}
      for i in range(len(nums)):
        if nums[i] in checkDict:
          return True
        else: 
          checkDict.update({nums[i] : i})
      return False



  


          