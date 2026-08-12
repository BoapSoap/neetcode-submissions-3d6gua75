class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for l in s:
            if l in hashmap: 
                hashmap[l] += 1
            if l not in hashmap:
                hashmap[l] = 1
        
        for l2 in t:
            if l2 not in hashmap:
                return False
            if hashmap[l2] == 0:
                return False
            if hashmap[l2] != 0: 
                hashmap[l2] -=1
        
        if sum(hashmap.values()) == 0:
            return True
        else: 
            return False


