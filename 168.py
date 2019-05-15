class Solution:
    def convertToTitle(self, n: int) -> str:
        #divide by 28
        import string
        mapping={}
        for index,s in enumerate(string.ascii_uppercase):
            mapping[index+1]=s
        mapping[0]="Z"
        result=""

        while n>26:
            tmp=n%26
            n=int(n/26)
            result=mapping[tmp]+result
        if n<=26:
            result=mapping[n]+result            
        return result
n=52
s=Solution()
a=s.convertToTitle(n)
print(a)