import random
import string
from random import choice
from random import randint

password_length = int(input("length"))
amount_numbers = int(input("numbers"))
amount_extra_symbols = int(input("extrasymbols"))
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
extra_symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
password = []
def letters(password_length,amount_numbers,amount_extra_symbols):
    for i in range(0, password_length - amount_numbers - amount_extra_symbols):
        random_letter = choice(string.ascii_letters)
        password.append(random_letter)
    checking_lower = any(letter.islower() for letter in password)
    checking_upper = any(letter.isupper() for letter in password)
    if checking_upper == False or checking_lower == False:
        print("false")
    return password

def numbers(password,amount_numbers):
    for i in range(amount_numbers):
        random_number = str(randint(0, 9))
        random_index = randint(0, len(password))
        password.insert(random_index, random_number)
    return password


def add_extra_symbols(password,amount_extra_symbols):
    for i in range(0,amount_extra_symbols):
        random_extra_symbols = random.choice(extra_symbols)
        random_index = randint(0, len(password))
        password.insert(random_index, random_extra_symbols)
    return password

def generate(password_length, amount_numbers, amount_extra_symbols):
    letters(password_length,amount_numbers,amount_extra_symbols)
    numbers(password,amount_numbers)
    add_extra_symbols(password,amount_extra_symbols)
    print("".join(password))


generate(password_length, amount_numbers,amount_extra_symbols) #Ограничения на цифры тоисть если всего элементов может быть
#30 то нельзя слишком много цифр тоисть количество букв это range(from_length,(till_length - amount numbers - extra_symbols)
