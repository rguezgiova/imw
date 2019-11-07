import sys

num = int(sys.argv[1])

if num <= 0:
    sys.exit('Escribe un número positivo')
else:
    for i in range(2, num):
        if num % i == 0:
            print ('No es primo!')
            break
    else:
        print ('Es primo!')
