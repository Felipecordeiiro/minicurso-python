"""
Retirados do Hackerrank
======= Exercício 1 =======
Task:
The provided code stub reads two integers and add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Example:
    a=3
    b=5
Print the following:
8
-2
15

Input Format:
The first line contains the first integer, a.
The second line contains the second integer, b.
"""

a = int(input("Insira o valor da variável a:"))
b = int(input("Insira o valor da variável b:"))

soma = a+b
sub = a-b
multi = a*b

print(f"{soma}\n{sub}\n{multi}")