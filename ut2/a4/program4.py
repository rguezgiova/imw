import sys

num = sys.argv[1:]
quant_num = len(num)
sum = 0

for i in num:
    i = float(i)
    sum += i
result = sum / quant_num
print(f"La media de los valores es: {result}")
