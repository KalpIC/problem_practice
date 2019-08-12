##from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Exercise 1 (and Solution)
#
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Enter Your Name = ")
age = int(input("Enter Your Age = "))

year100 = 2119-age

print("Hey", name,", you will turn 100 years old in", year100)
