"""Programa para indicar si el último dígito de un número de 4 cifras es par o impar"""

print("----------------------------------------------")
print("----------- NÚMEROS PARES O IMPARES ----------")
print("----------------------------------------------")

# input
x=input("Digite un número de 4 cifras: ")
x=int (x)

# processing
R = x % 10

U = R % 2

if U == 0:
    z = ("El número " + str (R) + " es par ")

else:
    z = ("El número " + str (R) + " es impar ")

# output 
print(z)