##part 3 of tic tac game
## From https://www.practicepython.org/




game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def print_game():
    print()
    for i in game:
        print("              ",i)
    print()
    print()

list=[]
print(list)

condi = True
condip1 = True
p1gotco_ordi = True
p2gotco_ordi = False


while condi ==True:
    while p1gotco_ordi ==True:
        print("          X X X X X                     P1 arena")
        p1x, p1y = int(input("x ")), int(input("y "))
        co_ordi = [p1x, p1y]

        if co_ordi in list:
            print("Place already marked")
            p2gotco_ordi = False
        else:
            list.append(co_ordi)
            game[p1x][p1y] = 'X'
            print_game()
            p2gotco_ordi = True
            p1gotco_ordi = False


    while p2gotco_ordi == True:
        print("          O O O O O                     P2 arena")
        p2x, p2y = int(input("x ")), int(input("y "))
        co_ordi = [p2x, p2y]


        if co_ordi in list:
            print("Place already marked")
            p1gotco_ordi = False
        else:
            list.append(co_ordi)
            game[p2x][p2y] = 'O'
            print_game()
            p1gotco_ordi = True
            p2gotco_ordi = False






































# a = '---'.join('    ')
# b = '   '.join('||||')
# print('\n'.join((a, b, a, b, a, b, a)))
#
# print(" --- --- --- \n|   |   |   |\n --- --- --- \n|   |   |   |\n --- --- --- \n|   |   |   |\n --- --- --- ")





