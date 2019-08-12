def gameboard(number):
    for i in range(number):
        print(number * ' ---')
        print((number + 1) * '|   ')
    print(number * ' ---')


if __name__=="__main__":
    number = int(input("Enter no. of nXn matrix game board"))
    gameboard(number)

    a = '---'.join('    ')
    b = '   '.join('||||')
    print('\n'.join((a, b, a, b, a, b, a)))