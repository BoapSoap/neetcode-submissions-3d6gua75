import string

class Solution:

    def uniqueValue(self, word: str) -> tuple:
        alphabet = {}

        for letter in string.ascii_lowercase:
            alphabet[letter] = 0
        
        for letter in word: 
            alphabet[letter] += 1
        
        return tuple(alphabet.values())
        


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_bank = {}

        for word in strs:
            signature = self.uniqueValue(word)

            if signature in word_bank:
                word_bank[signature].append(word)

            else:
                word_bank[signature] = [word]
            
        
        # next step is to take the values and  combine them into a single nested list

        return list(word_bank.values())






                

    
        
        