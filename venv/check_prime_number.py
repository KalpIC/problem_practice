n = int(input("Number : "))


def primefun(n):
    c = [i for i in range(2,n) if n % i == 0 ]

    if n > 1:
        if len(c) == 0:
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")



primefun(n)