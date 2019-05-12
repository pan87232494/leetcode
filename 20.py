"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        #stack if ([{ push, if }]), pop if stack top is same else return false
        stack=[]
        if s:
            for tmp in s:
                if tmp in ["(","[","{"]:
                    stack.append(tmp)
                elif tmp in [")","]","}"]:
                    if len(stack)>=1:
                        if tmp==")" and stack[-1]=="(":
                            stack.pop()                       
                        elif tmp=="]" and stack[-1]=="[":
                            stack.pop()
                                 
                        elif tmp=="}" and stack[-1]=="{":
                            stack.pop()
                        else:
                            return False
                    else:
                        return False            
                elif tmp=="":
                    pass
                else:
                    return False

        else:
            return True

        if len(stack)==0:
            return True
        else:
            return False



input="(])"
input="()"
s=Solution()
print(s.isValid(input))