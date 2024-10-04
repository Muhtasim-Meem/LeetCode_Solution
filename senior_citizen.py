def senior(details):
    count= 0
    for x in details:
        age = int(x[11:13])
        if age > 60:
            count += 1
    return count  

lst= ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(senior(lst))