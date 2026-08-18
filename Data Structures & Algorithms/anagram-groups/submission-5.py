class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      word_bank = {}

      for word in strs:
        signature = "".join(sorted(word))

        if signature in word_bank:
          word_bank[signature].append(word)
        else:
          word_bank[signature] = [word]

      return list(word_bank.values())  
        






  


 




