import random

# a = random.sample(range(1,25),24)
a = [1,2,3,4,8,6,5,1,5,7,9,2,3,5,56,21,12,25,7,46,5,323,1]
print(a)
b = []
# print([i for i in a if a.count(i)==1])
for i in a:
    if i not in b:
        b.append(i)

print(b)