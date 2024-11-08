"""
Retirados do Hackerrank
======= Desafio =======
Task:
ABC = 90º, in point B.
To find (angle tetha, as shown in the figure) in degrees.

Input Format:
The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format:

Output tetha in degrees.
Note: Round the angle to the nearest integer.
"""

import math

ab = int(input())
bc = int(input())

ac = math.sqrt(pow(bc, 2) + pow(ab, 2))
m_linha = ac/2

#sen(tetha)/m_linha=sen(90)/bc
#sen(tetha) = (1*m_linha)/bc

tetha = math.asin(m_linha/bc)
tetha_graus = round(math.degrees(tetha))

print(f"{tetha_graus}º")
