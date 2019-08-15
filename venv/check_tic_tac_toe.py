#
##
### From https://www.practicepython.org/
##
#

### take matrix from user
# matrix = []
# for j in range(3):
#     m1 = []
#     for i in range(3):
#         m = int(input("Enter your matrix no",))
#         m1.append(m)
#     matrix.append(m1)
# print(matrix)


matrix = [[2,1,1],[2,2,6],[8,1,2]]


player_1_win = [1,1,1]
player_2_win = [2,2,2]
p1 = False
p2 = False
diagonal2row = []
column2row = []


def row_check(function_matrix):
    global p1,p2
    for i in function_matrix:
        if i == player_1_win:
            p1 = True
        elif i == player_2_win:
            p2 = True

def column2rowfunc():
    for j in range(3):
        column_1 =[]
        for i in range(3):
            column_1.append(matrix[i][j])
        column2row.append(column_1)
    return column2row

def diagonal2rowfunc():
    diag_1 = []
    diag_2 = []
    for i in range(3):
        diag_1.append(matrix[i][i])
        diag_2.append(matrix[i][2-i])
    diagonal2row.append(diag_1)
    diagonal2row.append(diag_2)
    return diagonal2row



diagonal2rowfunc()   # converts diagonal to row
column2rowfunc()     # converts column to row


row_check(matrix)
row_check(column2row)
row_check(diagonal2row)

print()

if p1 == True and p2 == False:
    print("p1 wins")
elif p2 == True and p1 == False:
    print("P2 Wins")
else:
    print("Nobody Wins")

print()
print("p1 ",p1)
print("p2 ",p2)








# matrix_r = matrix[::-1]