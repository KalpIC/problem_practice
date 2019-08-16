#practice page or say rough diary

game = [['X','O','X'],
        [0,0,0],
        [0,0,0]]


a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b)))
# print('\n'.join((a, b, a, b, a, b, a)))
print("kk")

print(" --- --- --- \n|",game[0][0],"|",game[0][1],"|",game[0][2],"|\n"
      " --- --- --- \n|",game[1][0],"|",game[1][1],"|",game[1][2],"|\n "
      "--- --- --- \n|",game[2][0],"|",game[2][1],"|",game[2][2],"|","\n --- --- --- ")
count = 0
for i in range(20):
    count +=1
    print(count)