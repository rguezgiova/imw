import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100
adenine, thymine, guanine, cythosine = 0, 0, 0, 0

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

for nucleotide in sequence :
    if nucleotide == 'A':
        adenine +=1
    elif nucleotide == 'T':
        thymine +=1
    elif nucleotide == 'G':
        guanine +=1
    else:
        cythosine +=1

result = f'''Adenine: {adenine}
Guanine: {guanine}
Cythosine: {cythosine}
Thymine {thymine}'''
print(result)
