##
## From https://www.practicepython.org/
##
a = [1,1,2,3,4,1,2,4,7,5,3]
b = [2,2,4,5,6,2,3,4]
c = []


for i in a:
    if i in b:
        c.append(i)


print(c)