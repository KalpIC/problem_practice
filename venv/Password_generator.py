import string
import random

list = [string.ascii_letters,string.punctuation,string.digits]
password =[]
number = int(input("Enter Lenght of your password : "))

def randomletter():
    random_list = random.choice(list)
    random_letter = random.choice(random_list)
    return random_letter


for i in range(number):
    password.append(randomletter())

print("your password is ", "".join(password))






# lower_alpha = string.ascii_lowercase
# upper_alpha = string.ascii_uppercase

