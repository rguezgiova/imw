import sys

num = int(sys.argv[1])
string = sys.argv[2]
word, count = 0, 0
string = string + ' '

if num <= 0:
    sys.exit('Escribe un número positivo')
else:
    for char in string:
        if char != ' ':
            count += 1
        else:
            if count == num:
                word += 1
                count = 0
            else:
                count = 0
    print(f'Hay {word} palabras de tamaño {num}')
