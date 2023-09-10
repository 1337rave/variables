import math


try:
    a = float(input('Diagonal a = '))
    b = float (input('Diagonal a = '))
    print(f'S = (a*b)/2 = {(a*b)/2}')
except Exception as ex:
    print (ex)