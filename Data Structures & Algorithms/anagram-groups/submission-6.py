import string
class Solution:
    def encoding(self, word1: strs) -> tuple:
      hashmap = {}
      alphabet = string.ascii_lowercase

      for letter in alphabet: 
        hashmap[letter] = 0
      
      for letter in word1: 
        hashmap[letter] += 1

      return tuple(hashmap.values())






    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      word_bank = {}

      for word in strs:
        signature = self.encoding(word)

        if signature in word_bank:
          word_bank[signature].append(word)
        else:
          word_bank[signature] = [word]

      return list(word_bank.values())  
        






  


 




