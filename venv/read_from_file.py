
f = open("nametextfile.txt","r")
fr = f.read()
fr = fr.split('\n')
fr_name = []
for i in fr:
    if fr_name.count(i)==0:
        fr_name.append(i)

print(fr)
print(fr_name)
f.close()

