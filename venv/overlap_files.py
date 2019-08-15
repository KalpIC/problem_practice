fop = open("primenumbers.txt","r")  ##fop file overlap prime numbers
fopr = fop.read()
fopr_list = fopr.split('\n')
print("prime numbers = ", fopr_list)
fop.close()

foh = open("happynumbers.txt","r")     #foh file overlap happy numbers
fohr = foh.read()
fohr_list = fohr.split('\n')
print("happy numbers = ",fohr_list)
foh.close()


# fopr_int = int(fopr_list[len(fopr_list)-1])
# print("fopr int",fopr_int)

for i in range(len(fopr_list)-1):
    fopr_list[i]=int(fopr_list[i])
for i in range(len(fohr_list)-1):
    fohr_list[i]=int(fohr_list[i])


print("happy numbers (int) = ",fohr_list)
print("prime numbers (int) = ", fopr_list)

overlap_numbers = []

for i in fopr_list:
    if i in fohr_list:
        overlap_numbers.append(i)

print("overlap numbers are ",overlap_numbers)
print('there are',len(overlap_numbers),'numbers same in both files')