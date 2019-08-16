## From https://www.practicepython.org/
import sys

game = [[' ',' ' ,' '],
        [' ',' ' ,' '],
        [' ',' ' ,' ']]

matrix = game

player_1_win = ['X','X','X']
player_2_win = ['O','O','O']
p1 = False
p2 = False
diagonal2row = []
column2row = []

list=[]
print(list)

count = 0
condi = True
condip1 = True
p1gotco_ordi = True
p2gotco_ordi = False


def print_game():
    print(" --- --- --- \n|", game[0][0], "|", game[0][1], "|", game[0][2], "|\n"
            " --- --- --- \n|", game[1][0], "|",game[1][1], "|", game[1][2], "|\n "
             "--- --- --- \n|", game[2][0], "|", game[2][1], "|", game[2][2], "|",
             "\n --- --- --- ")
    print()
    print()

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

def win_p():
    if p1 == True and p2 == False:
        print(10*"p1 wins    ")
        sys.exit()
    elif p2 == True and p1 == False:
        print(10*"P2 Wins    ")
        sys.exit()

    p1gotco_ordi = False
    p2gotco_ordi = False

def move_counter():
    global count
    count +=1
    if count == 9:
        sys.exit("No more moves left....Bye Bye...")

print_game()

while condi == True:
    while p1gotco_ordi ==True:
        input_condi = True
        while input_condi==True:
            print("          X X X X X                     P1 arena")
            p1x, p1y = int(input("x ")), int(input("y "))
            if p1x > 2 or p1y > 2:
                input_condi = True
            else:
                input_condi = False




        co_ordi = [p1x, p1y]

        if co_ordi in list:
            print("Place already marked")
            p2gotco_ordi = False
        else:
            list.append(co_ordi)
            game[p1x][p1y] = 'X'
            print_game()
            diagonal2rowfunc()  # converts diagonal to row
            column2rowfunc()  # converts column to row
            row_check(matrix)
            row_check(column2row)
            row_check(diagonal2row)
            win_p()
            move_counter()
            p2gotco_ordi = True
            p1gotco_ordi = False


    while p2gotco_ordi == True:
        print("          O O O O O                     P2 arena")

        input2_condi = True
        while input2_condi == True:
            p2x, p2y = int(input("x ")), int(input("y "))

            if p2x>2 or p2y>2:
                input2_condi = True
            else:
                input2_condi = False

        co_ordi = [p2x, p2y]

        if co_ordi in list:
            print("Place already marked")
            p1gotco_ordi = False
        else:
            list.append(co_ordi)
            game[p2x][p2y] = 'O'
            print_game()
            diagonal2rowfunc()  # converts diagonal to row
            column2rowfunc()  # converts column to row
            row_check(matrix)
            row_check(column2row)
            row_check(diagonal2row)
            win_p()
            move_counter()
            p1gotco_ordi = True
            p2gotco_ordi = False







###############################

# matrix_r = matrix[::-1]
# a = '---'.join('    ')
# b = '   '.join('||||')
# print('\n'.join((a, b, a, b, a, b, a)))
#
# print(" --- --- --- \n|   |   |   |\n --- --- --- \n|   |   |   |\n --- --- --- \n|   |   |   |\n --- --- --- ")
