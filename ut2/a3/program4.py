import sys
import math

num = int(sys.argv[1])

if num < 0:
    sys.exit('Escribe un número positivo')
else:
    for i in range(1, num + 1):
        result = 1
        for j in range (i, 0, -1):
            result *= j
        print (i, '! =', result)
