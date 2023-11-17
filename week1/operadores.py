import math

print("=== OPERADORES DE ASIGNACION ===")
variables = "algo"

edad = 18
edad = edad + 5  #23
edad += 5   # edad = edad + 5 
print(edad)

nota = 20
nota /= 2 # nota = nota / 2
print(nota)

numero1 = 30
numero1 *= 53 #numero1 = numero1 * 53
print(numero1)

numero2 = 100
numero2 -= 190 #numero2 = numero2 - 90
print(numero2)

print("==== OPERADORES ARITMETICOS =====")
print(10 + 20)
print(10 - 20)
print(10 * 20)
print(10 / 20)
print(10 ** 20)
print(10 % 20)

#importamos math
print(math.sqrt(16))


print("==== OPERADORES DE COMPARACION====")
print(5=="5") #usamos == para comparar tanto valor como tipo de dato

print(5==5)
print("Hola" != 'hola') 
print(10>=10)
print(10>10)

