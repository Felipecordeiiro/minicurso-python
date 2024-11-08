"""
Retirados do Hackerrank
======= Exercício 3 =======
Task:
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Using math lib:
>>> pow(a, b)
Without math lib:
>>> a ** b

Input Format:
The first line contains a, the second line contains b, and the third line contains m.
"""

import math

a = int(input("Insira o valor de a:"))
b = int(input("Insira o valor de b:"))
m = int(input("Insira o valor de m:"))
pot = math.pow(a, b)
mod = pot % m

print(f"{pot}\n{mod}")