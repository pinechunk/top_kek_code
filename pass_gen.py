from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

pass_count = int(input('Количество генерируемых паролей:'))
pass_lens = int(input('Желаемая длинна паролей:'))
include_nums = input('Включать ли цифры 0123456789? (y/n)')
inc_ABC = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
inc_abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
inc_chars = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
inc_exo = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

chars = ''

if include_nums == 'y':
    chars += digits
if inc_ABC == 'y':
    chars += uppercase_letters
if inc_abc == 'y':
    chars += lowercase_letters
if inc_chars == 'y':
    chars += punctuation
if inc_exo == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(pass_lens, chars):
    password = ''
    for j in range(pass_lens):
        password += choice(chars)
    return password

for _ in range(pass_count):
    print(generate_password(pass_lens, chars))