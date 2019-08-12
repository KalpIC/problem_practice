n = int(input("Enter No."))

def fibonacci():

    if n ==0:
        fs = [0]
    elif n ==1:
        fs = [1]
    elif n==2:
        fs = [1,1]
    elif n>2 :
        fs = [1, 1]
        for i in range(n - 2):
            c = len(fs)
            x = fs[c - 1] + fs[c - 2]
            fs.append(x)



    return  print(fs)

fibonacci()
