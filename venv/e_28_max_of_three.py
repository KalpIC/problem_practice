import random


#user input method
# n1, n2, n3 = int(input("n1")), int(input("n2")), int(input("n3"))
# print(n1, n2, n3)

# using random method

n1 = random.randint(1,100)
n2 = random.randint(1,100)
n3 = random.randint(1,100)
print(n1, n2, n3)


maxis = ".......wait wait.....something went wrong"

if n1 > n2 and n1 > n3:
    maxis = n1
elif n2 > n1 and n2 > n3:
    maxis = n2
elif n3 > n1 and n3 > n2:
    maxis = n3
elif n1 == n2 or n2 == n3 or n1 == n3:
    if n1 > n2:
        maxis = n1
    elif n2 > n1:
        maxis = n2
    elif n3 > n1:
        maxis = n3
    elif n1 == n2 and n2 == n3:
        maxis = ".......All are Equal."

print("max of three is ", maxis)

