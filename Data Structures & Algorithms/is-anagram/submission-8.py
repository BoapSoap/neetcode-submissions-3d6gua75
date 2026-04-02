class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      hashmap = {}
      for n in s: 
        if n not in hashmap: 
          hashmap[n] = 0
        hashmap[n] += 1
      
      for m in t:
        if m not in hashmap: 
          return False
        
        if m in hashmap and hashmap[m] is not 0: 
          hashmap[m] -= 1
      
      if sum(hashmap.values()) == 0:
        return True
      else: 
        return False
        



        