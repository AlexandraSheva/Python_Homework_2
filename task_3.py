"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

n = int(input())
x = 2
status = True

while status:
    if x <= n:
        print (x)
        x*=2     
    else:
        status = False
        