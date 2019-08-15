
## test 001
#
# n,m = 1,100
#
# range_list = []
#
# def list():
#     for i in range(n,m):
#         range_list.append(i)
#
#
# condi = True
#
# while condi == True:
#     list()
#     print(range_list)
#     hl = input("is your element in this list 'yes' or 'no' ")
#     if hl == 'yes':
#         m = int((m/2)+1)
#     elif hl == 'no':
#         condi = False
#     range_list = []
#
#


#### incomplete

# list_1 = [i for i in range(100)]
#
# condi = True
# n = 50
# m = 0
# while condi==True:
#     n1 = n
#     print("My guess is ", list_1[n])
#     hl = input("Your Number compare to my guess is 'higher', 'lower' or 'exact' ?")
#     if hl == 'higher':
#         n = int(n + ((n-m) / 2))
#     elif hl == 'lower':
#         n = int(n-((n-m)/2))
#     elif hl == 'exact':
#         condi = False
#         print("I got you")
#     else:
#         print("entered something wrong , Try again")
#     m =n1
#     print("m = ",m)
#     print("n = ",n)




# n = 50
# prev = 0
# for i in range(10):
#     n1 =n
#     n = int(n+((n-prev)/2))
#     prev = n1
#     print("prev = ", prev)
#     print(n)