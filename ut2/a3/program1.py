import sys

num = int(sys.argv[1])

if num < 0:
    sys.exit('Escribe un número positivo')
else:
    for i in range(2, num + 1):
        if i % num == 0:
            print ('Es primo!')
            break
    else:
        print ('No es primo!')
