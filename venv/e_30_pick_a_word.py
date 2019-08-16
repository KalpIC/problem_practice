import random

file = open("sowpods.txt", 'r')
fr = file.read()
fr_list = fr.splitlines()
file.close()

number = int(input("How many words, you want print from sowpods.txt file? \nEnter Here..."))

sample = random.sample(range(0, len(fr_list)), number)

print("Your", number, "random words are")
for i in sample:
    print(fr_list[i])