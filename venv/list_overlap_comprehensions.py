import random

a = random.sample(range(1,30),12)
b = random.sample(range(1,30),16)

result = [i  for i in a if i in b]


resultone = [i for i in result if result.count(i) == 1 ]

print(a)
print(b)
print(result)
print(resultone)






# import random
#
# a = []
# b = []
# c = []
#
# for i in range(6):
#     a.append(random.randint(1,20))
# for i in range(10):
#     b.append(random.randint(1,20))
#
# for i in a:
#     if i in b:
#         c.append(i)
#
# print("list a is ",a)
# print("list b is ",b)
#
# print("common elements are ",c)
