import random

def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True #gotta play the game
    number = str(random.randint(0,9999)) #random 4 digit number
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")









##
###
####                       My Solutionn           ##
#####
######
#######

# import random
# import sys
#
# number = random.sample(range(0,9),4)
# print()
# print("Welcome to ""COW AND BULLS"" Game")
# print()
#
#
# def cow_bulls():
#     guess = input("Guess 4 Digit No.")
#     guess_list = [i for i in guess]
#     cow = 0
#     bulls = 0
#     for i in range(4):
#         if number[i] == int(guess_list[i]):
#             cow += 1
#         else:
#             bulls += 1
#
#     print("Cow =", cow, "bulls = ", bulls)
#     return [cow,bulls]
#
# trials = 0
# print(number)
# while 1:
#     cowbulls = cow_bulls()
#     if cowbulls == [4, 0]:
#         print()
#         print("You Won")
#         print()
#         print("It takes you ", trials, "trials")
#         sys.exit()
#     else:
#         print("Try Again")
#         trials += 1
#

