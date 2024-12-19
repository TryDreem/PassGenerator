import random
import string
import pyperclip
from random import choice
from random import randint
from colorama import Style, Fore

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
extra_symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
password = []
password_length = 8
amount_numbers = 1
amount_extra_symbols = 0
feature_clipboard = True


def main_menu():
    state = "off" if feature_clipboard else "on"
    print(f"{Fore.LIGHTMAGENTA_EX}Please enter the option...{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}1.Generate password\n{Fore.LIGHTGREEN_EX}"
          f"2.Mode \n{Fore.LIGHTCYAN_EX}3.Turn {state}\n{Fore.LIGHTRED_EX}4.Quit{Style.RESET_ALL}\n")
    choice = input()

    if choice == "1" or choice.lower() == "generate":
        generate(password_length, amount_numbers, amount_extra_symbols) #Launching generation
    elif choice == "2" or choice.lower() == "mode":
        mode_menu() #Moving to Mode Menu
    elif choice == "3" or choice.lower() == "turn on":
        change_feature_clipboard()
    elif choice == "4" or choice.lower() == "quit": #Quit
        print(f"{Fore.LIGHTWHITE_EX}PassGenerator made by {Fore.LIGHTCYAN_EX}{Style.BRIGHT}TryDreem")
    else: #Any answers
        print(f"{Fore.LIGHTWHITE_EX}Could you please enter option one more time :) ")
        main_menu()





def generate(password_length, amount_numbers, amount_extra_symbols):
    password.clear()
    letters(password_length,amount_numbers,amount_extra_symbols)
    numbers(password,amount_numbers)
    add_extra_symbols(password,amount_extra_symbols)
    generated_pass = "".join(password)
    print(generated_pass)
    if feature_clipboard:
        clipboard(generated_pass)



def clipboard(generated_pass):
    pyperclip.copy(generated_pass)


def change_feature_clipboard():
    global feature_clipboard
    feature_clipboard = not feature_clipboard
    main_menu()


def letters(password_length,amount_numbers,amount_extra_symbols):
    for i in range(0, password_length - amount_numbers - amount_extra_symbols):
        random_letter = choice(string.ascii_letters)
        password.append(random_letter)
    checking_lower = any(letter.islower() for letter in password)
    checking_upper = any(letter.isupper() for letter in password)
    if checking_upper == False or checking_lower == False:
        generate(password_length,amount_numbers,amount_extra_symbols)
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


def mode_menu():
    print(f"{Fore.LIGHTGREEN_EX}1.Complexity\n{Fore.LIGHTRED_EX}2.Go back{Style.RESET_ALL}")
    choice = input(f"{Fore.LIGHTMAGENTA_EX}Enter the option{Style.RESET_ALL}\n")
    if choice == "1" or choice.lower() == "complexity":
        complexity_menu()
    elif choice == "2" or choice.lower() == "go back":
        main_menu() #Going back to the main menu
    else:
        print(f"{Fore.LIGHTWHITE_EX}Could you please enter option one more time :) ")
        mode_menu()


def complexity_menu():
    print(f"{Fore.LIGHTGREEN_EX}1.Common\n{Fore.LIGHTYELLOW_EX}2.Hard\n{Fore.LIGHTMAGENTA_EX}3.Complicated\n"
          f"{Fore.LIGHTCYAN_EX}4.User preferences\n{Fore.LIGHTRED_EX}5.Go back{Style.RESET_ALL}")
    choice = input(f"{Fore.LIGHTMAGENTA_EX}Enter the option{Style.RESET_ALL}\n")
    if choice == "1" or choice.lower() == "common":
        common_complexity()
    elif choice == "2" or choice.lower() == "hard":
        hard_complexity()
    elif choice == "3" or choice.lower() == "complicated":
        complicated_complexity()
    elif choice == "4" or choice.lower() == "user preferences":
        user_preferences()
    elif choice == "5" or choice.lower() == "go back":
        mode_menu() #Going back to the mode menu
    else:
        print(f"{Fore.LIGHTWHITE_EX}Could you please enter option one more time :) ")
        complexity_menu()


def settings_common_complexity():
    global password_length, amount_numbers, amount_extra_symbols
    password_length = 8
    amount_numbers = 1
    amount_extra_symbols = 0
    return password_length, amount_numbers, amount_extra_symbols


def common_complexity():
    settings_common_complexity()
    main_menu()


def settings_hard_complexity():
    global password_length, amount_numbers, amount_extra_symbols
    password_length = 12
    amount_numbers = randint(2, 4)
    amount_extra_symbols = 1
    return password_length, amount_numbers, amount_extra_symbols


def hard_complexity():
    settings_hard_complexity()
    main_menu()


def settings_complicated_complexity():
    global password_length, amount_numbers, amount_extra_symbols
    password_length = 20
    amount_numbers = randint(3, 6)
    amount_extra_symbols = randint(2, 4)
    return password_length, amount_numbers, amount_extra_symbols


def complicated_complexity():
    settings_complicated_complexity()
    main_menu()


def user_preferences():
    print(f"{Fore.LIGHTGREEN_EX}1.Length\n{Fore.LIGHTYELLOW_EX}2.Symbols{Fore.LIGHTRED_EX}\n3.Go back{Style.RESET_ALL}")
    choice = input(f"{Fore.LIGHTMAGENTA_EX}Enter the option{Style.RESET_ALL}\n")
    if choice == "1" or choice.lower() == "length":
        length()
    elif choice == "2" or choice.lower() == "symbols":
        symbols()
    elif choice == "3" or choice.lower() == "go back":
        complexity_menu()
    else:
        print(f"{Fore.LIGHTWHITE_EX}Could you please enter option one more time :) ")
        user_preferences()


def length():
    print(f"{Fore.LIGHTWHITE_EX}Now length is {Fore.LIGHTCYAN_EX}{password_length}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}1.Change length\n{Fore.LIGHTRED_EX}2.Go Back{Style.RESET_ALL}")
    choice = input()
    if choice == "1" or choice.lower() == "change length":
        change_length()
    elif choice == "2" or choice.lower() == "go back":
        user_preferences()
    else:
        print(f"{Fore.LIGHTWHITE_EX}Could you please enter option one more time :) ")
        length()


def settings_change_length():
    global password_length
    print(f"{Fore.LIGHTWHITE_EX}Minimal length is {Fore.LIGHTRED_EX}8{Style.RESET_ALL}")
    password_length = int(input(f"{Fore.LIGHTWHITE_EX}Enter a new length...{Style.RESET_ALL}"))
    return password_length


def change_length():
    settings_change_length()
    length()


def symbols():
    print(f"{Fore.LIGHTWHITE_EX}Now amount of symbols:  amount of numbers - {Fore.LIGHTGREEN_EX}{amount_numbers}"
          f"{Fore.LIGHTWHITE_EX} and amount of extra symbols - {Fore.LIGHTYELLOW_EX}{amount_extra_symbols}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}1.Change amount of numbers\n"
          f"{Fore.LIGHTYELLOW_EX}2.Change amount of extra symbols\n"
          f"{Fore.LIGHTRED_EX}3.Go Back{Style.RESET_ALL}")
    choice = input()
    if choice == "1":
        change_amount_of_numbers()
    elif choice == "2":
        change_amount_of_extra_symbols()
    elif choice == "3":
        user_preferences()
    else:
        print(f"{Fore.LIGHTWHITE_EX}Could you please enter option one more time :) ")
        symbols()


def settings_change_amount_of_numbers():
    global amount_numbers
    amount_numbers = int(input(f"{Fore.LIGHTWHITE_EX}Enter a new amount of numbers...{Style.RESET_ALL}"))
    return amount_numbers


def change_amount_of_numbers():
    settings_change_amount_of_numbers()
    symbols()


def settings_change_amount_of_extra_symbols():
    global amount_extra_symbols
    amount_extra_symbols = int(input(f"{Fore.LIGHTWHITE_EX}Enter a new amount of numbers...{Style.RESET_ALL}"))
    return amount_extra_symbols


def change_amount_of_extra_symbols():
    settings_change_amount_of_extra_symbols()
    symbols()


main_menu()

#сделать чтобы кол-во цыфр или знаков не превышало допустимое значение
#если возможно добавить какой режим текущий
