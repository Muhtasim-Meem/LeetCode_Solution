class Solution(object):
    def addToArrayForm(self, num, k):
        res= 0
        ans = []
        for x in num:
            res=res*10+x

        y = res+k

        while y > 0:
            z=y%10
            ans.append(z)

            y = y//10

        ans.reverse()
        return ans  