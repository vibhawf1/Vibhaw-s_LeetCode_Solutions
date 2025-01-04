class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a,b = 0, x
        while b>9:
            a+=b%10
            b=b//10
        a+=b
        return -1 if not x%a==0 else a
