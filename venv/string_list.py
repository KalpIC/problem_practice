#   Ask the user for a string and print out whether this string is a palindrome or not.
#   (A palindrome is a string that reads the same forwards and backwards.)
#    https://www.practicepython.org/
#

string = str(input("enter any word :"))

l1 = string
l2 = string[::-1]
print(l1)
print(l2)
if l1 == l2:
    print("Word is palindrome")
else:
    print('nothing')

######   . . l1 = []  l2 = []
### or >>> for i in string:    l1.append(i)
### or >>> for i in reversed(string): l2.append(i)
