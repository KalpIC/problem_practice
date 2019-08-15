def gameboard(size):
    for i in range(size):
        print(size * ' ---')
        print((size + 1) * '|   ')
    print(size * ' ---')


if __name__=="__main__":
    number = int(input("Enter size of game board matrix"))
    gameboard(number)


    ## internet solution

    a = '---'.join('    ')
    b = '   '.join('||||')
    print('\n'.join((a, b, a, b, a, b, a)))