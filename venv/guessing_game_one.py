

import random

n = random.randint(1,9)  #### random number
guess = 0
count = 0

while guess != n and guess != "exit":
    guess = input("What's your guess?")

    if guess == "exit":
        break


    guess = int(guess)
    count += 1

    if guess < n:
        print("Too low!")
    elif guess>n:
        print("Too High")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")







































# import sys
# import random
# i = 'a'
#
# ###########
# ###########
# ##########                                  code in building phase
# #############
# #########################
# def guessno():
#     r = random.randint(1, 9)
#     rlist = [r - 2, r - 1, r + 1, r + 2]
#     n = int(input("Guess any no. b/w 1 to 9"))
#
#     if n == r:
#         print("exact no.")
#     elif n in rlist:
#         print("near about")
#     else:
#         print("too far")
#
#     print('random no. is',r)
#
#
#     i = input("b for quit")
#
# guessno()
#
# while True:
#     if i == 'a':
#         guessno()
#     elif i == 'b':
#         sys.exit()