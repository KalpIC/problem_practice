##
## From https://www.practicepython.org/
##
x = int(input("Enter Any Number : "))
y = []

for i in range (1,x+1):
    if x % i==0:
        y.append(i)


print(y)

z = x
y1 =[]

for i in range(1,z):
    if x%i==0:
        y1.append(i)
        z= z/i
y1.append(x)
print(y1)