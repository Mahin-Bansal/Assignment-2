import math
l = float(input("Enter slant length :") )
a = math.pi/4
h = l * math.sin(a)
r = l * math.cos(a)
V = math.pi * r* r*h/3
print("Please enter rate of change of Volume")
#let dl/dt be U
U = float(input())
print("The change of l be Denoted by Z and its value iw ")
Z = l * U /(V * 3)
print(Z)