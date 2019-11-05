import sys
import math

num = int(sys.argv[1])
result = 0

if num < 0:
    sys.exit('Escribe un número positivo')
else:
    for i in range(1, num + 1):
        result += i ** 2
    print (result)
