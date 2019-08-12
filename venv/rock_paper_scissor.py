print("introduction to game and how to play here")
print(" enter 1 for Rock,\n enter 2 for Scissor,\n enter 3 for paper.")



# def p1limit():
#     p1 = int(input("Player 1 \n Make Your Move: "))
#     if p1 != [1,2,3]:
#         print("Out of Game, Enter Again")
#         p1
#
#
# def p2limit():
#     p2 = int(input("Player 2 \n Make Your Move: "))
#     if p2 != [1,2,3]:
#         print("Out of Game, Enter Again")
#         return p2
# p1limit()
# p2limit()




def rpcgame():
    p1 = int(input("Player 1 \n Make Your Move: "))
    p2 = int(input("Player 2 \n Make Your Move: "))

    p1wins = [(1, 2), (2, 3), (3, 1)]
    p2wins = [(1, 3), (2, 1), (3, 2)]
    tie = [(1, 1), (2, 2), (3, 3)]

    if (p1, p2) in p1wins:
        print()
        print("P1 Wins")
        print()
    elif (p1, p2) in p2wins:
        print()
        print("P2 Wins")
        print()
    elif (p1, p2) in tie:
        print()
        print("..tie..")
        print()
    else:
        print()
        print("Playing Out of Game")
        print()

rpcgame()

restart = input("Enter 'restart' to restart game")

while True:
    restart = 'restart'
    rpcgame()



















