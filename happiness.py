def maximumHappinessSum(happiness,k):
    happiness.sort()

    mx=0
    while k !=0:
        mx+=happiness[-1]
        happiness.pop(-1)
        for i in range(len(happiness)):
            if happiness[i] > 0:
                happiness[i]-=1        
        k-=1
    return mx

hap=[1,1,1,1]
k=2
print(maximumHappinessSum(hap,k))

## TLE ##

def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)

        sums=0

        for i in range(k):
            p=max(happiness[i]-i,0)
            sums+=p
        return sums    

## Accepted 