import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if a < 0 or b < 0:
    sys.exit('Escribe dos números positivos')
else:
    if a < b:
        c = a
    else:
        c = b
    for i in range(c, 0, -1):
        if a % i == 0:
            if b % i == 0:
                print (i)
                break
