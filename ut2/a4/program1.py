import sys

num = int(sys.argv[1])
letter = 'TRWAGMYFPDXBNJZSQVHLCKE'

remain = num % 23

print(f'{num}{letter[remain]}')
