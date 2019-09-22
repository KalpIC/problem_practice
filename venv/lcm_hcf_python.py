a,b = int(input("a : ")),int(input("b : "))
c = a
d = b
ab_list = []
j =0


if a>b:
    g = int(a/2)
else:
    g = int(b/2)

prime_list = []


for num in range(g + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break 
        else:
            prime_list.append(num)
            


def mul_func(list1):
    m = 1
    for i in list1:
        m = m*i
    return m


p = prime_list[0]

while(True):
    if a%p==0 or b%p==0:
        ab_list.append(p)
        if a%p == 0:
            a = a/p
        if b%p == 0:
            b = b/p
    else:
        if j==len(prime_list):
            break
        p = prime_list[j]
        j=j+1
    
print("LCM is :",mul_func(ab_list))




####### hcf

al = []
bl = []
ll = []

def factors(x,l):
    for i in range(1,int(x/2)+1):
        if x%i==0:
            l.append(i)


factors(c,al)
factors(d,bl)

for i in al:
    if i in bl:
        ll.append(i)

ll.sort()
print("hcf is : ",ll[-1])
        

