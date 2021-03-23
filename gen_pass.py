# from string import printable
from random import randint

SYMB = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

password = ''


def ran_sym():
    return randint(0, len(SYMB) - 1)


def generate(num):
    global password
    if num == 0:
        return password
    password += SYMB[ran_sym()]
    num -= 1
    return generate(num)


num = int(input('Введите длинну пароля: '))
print(generate(num))
print()
