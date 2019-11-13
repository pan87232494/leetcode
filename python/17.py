# 17. Letter Combinations of a Phone Number
# Medium
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution:
    def letterCombinations(self, digits: str):
        mapping={
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        result=[]
        for s in digits:
            if s in mapping:
                if result==[]:
                    for tmp2 in mapping[s]:
                        result.append(tmp2)
                    result_new=result
                else:
                    result_new=[]
                    for tmp2 in mapping[s]:     
                        for index,tmp in enumerate(result):                       
                            tmp=tmp+tmp2
                            result_new.append(tmp)
                result=result_new
                
            else:
                exit(1)
        return result

input="23"
s=Solution()
print(s.letterCombinations(input))