import math

try:
    a = int(input ("a: "))
    b = int(input ("b: "))
    c = int(input ("c: "))
    print(a+b+c)
    print(a*b*c)
except Exception as ex:
    print (ex)