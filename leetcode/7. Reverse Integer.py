class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        while x%10 == 0:
            x=x//10
        if x>0:
            k=str(x)[::-1]
        if x<0:
            k="-"+str(abs(x))[::-1]
        if int(k)>=2147483647 or int(k)<=-2147483648:
            return 0
        return k
