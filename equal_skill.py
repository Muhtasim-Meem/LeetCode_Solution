def skills(skill):
    skill.sort()
    target=skill[0]+skill[-1]
    l=0
    r=len(skill)-1
    total=0

    while l < r:

        if skill[l]+skill[r] != target:
            return -1
        else:
            total+=skill[l]*skill[r]
            l+=1
            r-=1
    return total

skill=[3,2,5,1,3,4]   
res=skills(skill)
print(res)     


