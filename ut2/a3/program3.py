import sys

vara = int(sys.argv[1])
varb = int(sys.argv[2])

if vara < 0 or varb < 0:
    sys.exit('Escribe dos números positivos')
else:
    if vara < varb:
        varc = vara
    else:
        varc = varb
    for i in range(varc, 0, -1):
        if vara % i == 0:
            if varb % i == 0:
                print (i)
                break
